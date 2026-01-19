import sys
import torch
import umap
import matplotlib.pyplot as plt
from transformers import CLIPModel, CLIPProcessor

# Get file path from command line or use default
path = sys.argv[1] if len(sys.argv) > 1 else "wiki_selection.txt"

# Read text file
with open(path, "r", encoding="utf-8") as f:
    text = f.read().lower()

# Extract tokens (words) from text
tokens = []
for word in text.split():
    cleaned = word.strip(".,!?;:\"'()[]{}")
    if cleaned:
        tokens.append(cleaned)

# Get unique tokens
tokens = sorted(set(tokens))

if not tokens:
    print("No tokens found.")
    raise SystemExit(0)

# Load CLIP model
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Get embeddings for all tokens
inputs = processor(text=tokens, return_tensors="pt", padding=True)
with torch.no_grad():
    features = model.get_text_features(**inputs)

# Normalize embeddings
features = features / features.norm(dim=-1, keepdim=True)

# Reduce to 2D using UMAP
reducer = umap.UMAP(n_neighbors=5, min_dist=0.2, random_state=42)
points = reducer.fit_transform(features.numpy())

# Plot results
plt.figure(figsize=(14, 12))
plt.scatter(points[:, 0], points[:, 1], s=10)
plt.title("CLIP Token Embeddings (UMAP)")
plt.xticks([])
plt.yticks([])
plt.tight_layout()
plt.savefig("week6_text_file_umap.png", dpi=150)
plt.show()
