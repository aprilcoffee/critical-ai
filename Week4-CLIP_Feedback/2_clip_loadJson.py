from PIL import Image
import requests 
from transformers import CLIPProcessor, CLIPModel

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

import json
with open('countries.json', 'r') as f:
    data = json.load(f)

countries = []
for item in data:
    countries.append(item['name'])


while True:
        
    url = 'https://thispersondoesnotexist.com/'
    img = Image.open(requests.get(url, stream=True).raw).convert("RGB")

    inputs = processor(text=countries, images=img, return_tensors="pt", padding=True)
    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image  # this is the image-text similarity score
    probs = logits_per_image.softmax(dim=1)  # we can take the softmax to get the label probabilities

    # Get the index of the emotional keyword with the highest probability
    index_of_highest_prob = probs.argmax().item()
    # Get the emotional keyword with the highest probability
    highest_prob_emotion = countries[index_of_highest_prob]

    # Get the corresponding probability
    highest_prob = probs[0, index_of_highest_prob].item()

    print(f"Highest probability emotion: {highest_prob_emotion}\tProbability: {highest_prob:.2f}")

    img.save(f'./this.jpg')
