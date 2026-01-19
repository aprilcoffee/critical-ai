import os
import torch
import umap
import plotly.graph_objects as go
from PIL import Image
from transformers import CLIPModel, CLIPProcessor
import base64
from io import BytesIO

# Find images folder in same directory as this script
script_dir = os.path.dirname(__file__)
folder = os.path.join(script_dir, "images")

# Find all image files
image_paths = []
for root, dirs, files in os.walk(folder):
    for filename in files:
        extension = os.path.splitext(filename)[1].lower()
        if extension in [".jpg", ".jpeg", ".png", ".bmp", ".gif"]:
            full_path = os.path.join(root, filename)
            image_paths.append(full_path)

if not image_paths:
    print(f"No images found in {folder}")
    raise SystemExit(0)

# Sort paths and load images
image_paths = sorted(image_paths)
images = []
for path in image_paths:
    img = Image.open(path).convert("RGB")
    images.append(img)

# Load CLIP model
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Get embeddings for all images
inputs = processor(images=images, return_tensors="pt", padding=True)
with torch.no_grad():
    features = model.get_image_features(**inputs)

# Normalize embeddings
features = features / features.norm(dim=-1, keepdim=True)

# Reduce to 2D using UMAP
reducer = umap.UMAP(n_neighbors=5, min_dist=0.2, random_state=42)
points = reducer.fit_transform(features.numpy())

# Convert images to base64 for display
def image_to_base64(img, size=(64, 64)):
    img_resized = img.resize(size)
    buffered = BytesIO()
    img_resized.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return f"data:image/png;base64,{img_str}"

# Get axis ranges for scaling
x_min, x_max = points[:, 0].min(), points[:, 0].max()
y_min, y_max = points[:, 1].min(), points[:, 1].max()
x_range = x_max - x_min
y_range = y_max - y_min

# Create scatter plot
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=points[:, 0],
    y=points[:, 1],
    mode='markers',
    marker=dict(size=10, opacity=0.3, color='blue'),
    showlegend=False,
))

# Add images directly on the plot
for point, img in zip(points, images):
    x, y = point[0], point[1]
    
    # Normalize coordinates to 0-1 range for image positioning
    x_norm = (x - x_min) / x_range if x_range > 0 else 0.5
    y_norm = (y - y_min) / y_range if y_range > 0 else 0.5
    
    # Convert image to base64
    img_base64 = image_to_base64(img, size=(64, 64))
    
    # Add image annotation
    fig.add_layout_image(
        dict(
            source=img_base64,
            xref="x",
            yref="y",
            x=x,
            y=y,
            sizex=x_range * 0.1,
            sizey=y_range * 0.1,
            xanchor="center",
            yanchor="middle",
            layer="above",
        )
    )

fig.update_layout(
    title="CLIP Image Embeddings (Interactive UMAP)",
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[x_min - x_range*0.1, x_max + x_range*0.1]),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[y_min - y_range*0.1, y_max + y_range*0.1]),
    width=1200,
    height=800,
)

fig.show()

# Calculate and print average embedding
average_embedding = features.mean(dim=0)
print("Average embedding:", average_embedding.tolist())
