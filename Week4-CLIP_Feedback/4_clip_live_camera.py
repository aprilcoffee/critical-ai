from PIL import Image
import cv2
from transformers import CLIPProcessor, CLIPModel
import torch

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

texts = [   "Smoked Salmon",
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
    "kimchi",]

cap = cv2.VideoCapture(1)

print("Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(rgb_frame)
    
    # Process with CLIP
    inputs = processor(text=texts, images=pil_image, return_tensors="pt", padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = outputs.logits_per_image.softmax(dim=1).squeeze()
    
    # Get best match
    best_idx = probs.argmax().item()
    best_text = texts[best_idx]
    best_prob = probs[best_idx].item()
    
    # Display on frame
    # Sort scores and display all ranked results on the frame
    sorted_indices = probs.argsort(descending=True)
    for rank, idx in enumerate(sorted_indices):
        text = texts[idx]
        prob = probs[idx].item()
        y = 30 + rank * 35
        cv2.putText(frame, f"{rank+1}. {text}: {prob:.2f}", (10, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow('CLIP Live Camera', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

