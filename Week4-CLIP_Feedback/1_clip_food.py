from PIL import Image
import requests 
from transformers import CLIPProcessor, CLIPModel

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# List of emotional keywords
food_keywords = [
    "Smoked Salmon",
    "schnitzel",
    "Jollof rice",
    "tajine",
    "Macaroni and cheese",
    "Curry Wurst",
    "Pizza",
    "Nasi Lemak",
    "Sauce Mole",
    "Fried Rice",
    "Katsudon",
    "Crepe",
    "kimchi",
]

url = 'https://thispersondoesnotexist.com/'
img = Image.open(requests.get(url, stream=True).raw).convert("RGB")

#img = Image.open("european-person.png")
img = img.resize((512, 512))

# Convert the image to RGB format if it's not already
if img.mode != 'RGB':
    img = img.convert('RGB')

inputs = processor(text=food_keywords, images=img, return_tensors="pt", padding=True)

outputs = model(**inputs)
logits_per_image = outputs.logits_per_image  # this is the image-text similarity score
probs = logits_per_image.softmax(dim=1)  # we can take the softmax to get the label probabilities
index_of_highest_prob_food = probs.argmax().item()
highest_prob_food = food_keywords[index_of_highest_prob_food]

# Get the corresponding probability
highest_prob = probs[0, index_of_highest_prob_food].item()

print(f"Highest probability food: {highest_prob_food}\tProbability: {highest_prob:.2f}")

#print(f"{i}\tscore: {now:.2f}")
for j, food in enumerate(food_keywords):
    prob_food = probs[0, j].item()
    print(f"food: {food}\tProbability: {prob_food:.2f}")


