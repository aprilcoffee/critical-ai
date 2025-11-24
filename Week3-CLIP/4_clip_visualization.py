from PIL import Image
import requests
from transformers import CLIPProcessor, CLIPModel
import torch
import matplotlib.pyplot as plt
import numpy as np

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw).convert("RGB")

texts = ["a cat", "a dog", "a person", "an animal", "a pet"]

with torch.no_grad():
    image_emb = model.get_image_features(**processor(images=image, return_tensors="pt"))
    text_embs = model.get_text_features(**processor(text=texts, return_tensors="pt", padding=True))
    image_emb = image_emb / image_emb.norm()
    text_embs = text_embs / text_embs.norm(dim=-1, keepdim=True)
    similarities = (image_emb @ text_embs.T).squeeze().numpy()

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
bars = plt.barh(texts, similarities, color='skyblue')
bars[np.argmax(similarities)].set_color('red')
plt.xlabel('Similarity')
plt.title('Similarity Scores')

plt.subplot(1, 2, 2)
plt.scatter(image_emb[0, 0].item(), image_emb[0, 1].item(), s=200, c='red', marker='*', label='Image')
for i, text in enumerate(texts):
    plt.scatter(text_embs[i, 0].item(), text_embs[i, 1].item(), label=text, alpha=0.7)
plt.xlabel('Dim 1')
plt.ylabel('Dim 2')
plt.title('Embeddings (2D)')
plt.legend(fontsize=8)

plt.tight_layout()
plt.savefig('clip_visualization.png')
print("Saved: clip_visualization.png")
plt.show()

