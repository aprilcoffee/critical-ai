from PIL import Image
import requests
from transformers import CLIPProcessor, CLIPModel

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw).convert("RGB")

texts = ["a cat", "a dog", "a person"]
inputs = processor(text=texts, images=image, return_tensors="pt", padding=True)

tokenizer = processor.tokenizer

print("Tokenization:")
for text in texts:
    tokens = tokenizer.tokenize(text)
    print(f"'{text}' -> {tokens}")

print(f"\nInput shape: {inputs['input_ids'].shape}")
print(f"Token IDs:\n{inputs['input_ids']}")

outputs = model(**inputs)
probs = outputs.logits_per_image.softmax(dim=1)

print("\nSimilarities:")
for i, text in enumerate(texts):
    print(f"{text}: {probs[0][i].item():.3f}")

