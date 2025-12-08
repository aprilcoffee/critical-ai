from ollama import chat
import cv2
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import threading

cap = cv2.VideoCapture(1)
if not cap.isOpened():
    cap = cv2.VideoCapture(0)
temp_image_path = "/tmp/llava_capture.jpg"
response_text = None
current_frame = None
processing = False

def process_question():
    global response_text, current_frame, processing
    while True:
        prompt = input()
        if prompt and current_frame is not None:
            processing = True
            cv2.imwrite(temp_image_path, current_frame)
            abs_path = os.path.abspath(temp_image_path)
            if os.path.exists(abs_path):
                result = chat(
                    model='llava',
                    messages=[{
                        'role': 'user',
                        'content': f'{prompt} {abs_path}'
                    }]
                )
                response_text = result['message']['content']
                print(f"LLaVA: {response_text}")
            else:
                print("Error: Image file not saved")
            processing = False

input_thread = threading.Thread(target=process_question, daemon=True)
input_thread.start()

print("Camera feed running. Type your question and press Enter.")
print("Press 'q' in the window to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    current_frame = frame.copy()
    display_frame = frame.copy()
    
    if response_text:
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(rgb_frame)
        draw = ImageDraw.Draw(pil_image)
        font = ImageFont.load_default()
        
        words = response_text.split(' ')
        y = 10
        line = ""
        for word in words:
            test_line = line + word + " "
            if len(test_line) > 60:
                draw.text((10, y), line, font=font, fill=(255, 255, 255))
                y += 20
                line = word + " "
            else:
                line = test_line
        if line:
            draw.text((10, y), line, font=font, fill=(255, 255, 255))
        
        display_frame = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    
    if processing:
        cv2.putText(display_frame, "Processing...", (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    else:
        cv2.putText(display_frame, "Type question in terminal", 
                   (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    
    cv2.imshow('LLaVA Live Camera', display_frame)
    
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
