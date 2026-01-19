import torch
from transformers import CLIPModel, CLIPProcessor

# Load CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Input sentence
sentence = "A small cat sits on a mat."

# Process text into format CLIP expects
inputs = processor(text=[sentence], return_tensors="pt", padding=True)

# Get embedding (disable gradient for inference)
with torch.no_grad():
    embedding = model.get_text_features(**inputs)[0]

# Normalize embedding
embedding = embedding / embedding.norm()

# Print results
print("Sentence:", sentence)
print("Embedding:", embedding.tolist())
