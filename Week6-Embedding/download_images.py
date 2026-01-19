import requests
from PIL import Image
from io import BytesIO
import os

os.makedirs("images", exist_ok=True)

for i in range(10):
    url = f"https://picsum.photos/512/512?random={i}"
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.save(f"images/image_{i:02d}.jpg")
    print(f"Downloaded image_{i:02d}.jpg")

print("Done! 10 images downloaded to images/ folder")
