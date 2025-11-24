from PIL import Image
import requests
from transformers import CLIPProcessor, CLIPModel

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw).convert("RGB")

texts = ["a cat", "a dog", "a person", "an animal", "a pet"]

inputs = processor(text=texts, images=image, return_tensors="pt", padding=True)
outputs = model(**inputs)
scores = outputs.logits_per_image.squeeze().tolist()
probs = outputs.logits_per_image.softmax(dim=1).squeeze().tolist()

results = list(zip(texts, scores, probs))
results.sort(key=lambda x: x[1], reverse=True)

print("Ranked results:")
for i, (text, score, prob) in enumerate(results, 1):
    print(f"{i}. {text:15s} | Score: {score:6.2f} | Prob: {prob*100:5.1f}%")

