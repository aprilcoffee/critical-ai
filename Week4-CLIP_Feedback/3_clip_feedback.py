from PIL import Image
import requests 
from transformers import CLIPProcessor, CLIPModel
import os

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

#url = "http://images.cocodataset.org/val2017/000000039769.jpg"
#image = Image.open(requests.get(url, stream=True).raw)

# Create output directory if it doesn't exist
os.makedirs('./outputimage', exist_ok=True)

happiness = 0.0
sadness = 100.0
i = 0
while True:
    i=i+1
    
    """
    https://www.placecage.com/512/512

https://placekitten.com/512/512

https://picsum.photos/512/512

https://thiscatdoesnotexist.com/
    """

    url = 'https://thispersondoesnotexist.com/'
    img = Image.open(requests.get(url, stream=True).raw).convert("RGB")

    inputs = processor(text=["happy"], images=img, return_tensors="pt", padding=True)

    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image  # this is the image-text similarity score
    #probs = logits_per_image.softmax(dim=1)  # we can take the softmax to get the label probabilities
    
    now = logits_per_image.item()
   
    print(f"{i}\tnow:{now}\tmax:{happiness}\tmin:{sadness}")
    if(now > happiness):
        happiness = now
        img.save('./outputimage/happiestImage.jpg')
    if(now < sadness):
        sadness = now
        img.save('./outputimage/sadestImage.jpg')
    img.save('./outputimage/this.jpg')