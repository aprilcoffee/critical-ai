import torch
import umap
import matplotlib.pyplot as plt
from transformers import CLIPModel, CLIPProcessor

# Load CLIP model
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# List of texts to embed
texts = [
    "a cat",
    "a dog",
    "a red car",
    "a blue car",
    "a sunny beach",
    "a rainy city",
    "a slice of pizza",
    "a bowl of salad",
]

# Get embeddings for all texts
inputs = processor(text=texts, return_tensors="pt", padding=True)
with torch.no_grad():
    features = model.get_text_features(**inputs)

# Normalize embeddings
features = features / features.norm(dim=-1, keepdim=True)

# Reduce to 2D using UMAP
reducer = umap.UMAP(n_neighbors=5, min_dist=0.2, random_state=42)
points = reducer.fit_transform(features.numpy())

# Plot results
plt.figure(figsize=(6, 5))
plt.scatter(points[:, 0], points[:, 1])

# Add text labels
for i, label in enumerate(texts):
    plt.text(points[i, 0], points[i, 1], label, fontsize=9)

plt.title("CLIP Text Embeddings (UMAP)")
plt.xticks([])
plt.yticks([])
plt.tight_layout()
plt.savefig("week6_text_umap.png", dpi=150)
plt.show()
