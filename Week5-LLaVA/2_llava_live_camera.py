import cv2
import threading
from ollama import chat
import os
import time

def speak(text):
    """
    Use macOS 'say' command to speak the given text aloud.
    """
    os.system(f'say "{text}"')

# === EDIT THIS ===
question = "You are a comedian. Directly Roast this person in ONE SINGLE sentences, no list, and no extra commentary."

# === CAMERA (cross-platform) ===
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    cap = cv2.VideoCapture(1)
if not cap.isOpened():
    raise RuntimeError("No camera found")

cv2.namedWindow('LLaVA Live', cv2.WINDOW_NORMAL)  # helps Mac show the window

response_text = ""
processing = False
current_frame = None

def ask():
    """Send a snapshot + the global question to LLaVA in a background thread."""
    global processing
    if current_frame is None or processing:
        return
    snapshot = current_frame.copy()
    processing = True

    def run():
        global response_text, processing
        try:
            ok, buf = cv2.imencode('.jpg', snapshot)
            if not ok:
                return
            result = chat(
                model='gemma3:4b',
                messages=[{
                    'role': 'user',
                    'content': question,
                    'images': [buf.tobytes()],
                }]
            )
            response_text = result['message']['content']
            print(f"\n[Q] {question}\n[A] {response_text}\n")
            speak(response_text)
        finally:
            processing = False

    threading.Thread(target=run, daemon=True).start()

def wrap(text, max_chars):
    lines, line = [], ""
    for word in text.split():
        if len(line) + len(word) + 1 > max_chars:
            lines.append(line)
            line = word
        else:
            line = (line + " " + word).strip()
    if line:
        lines.append(line)
    return lines

def draw_text(frame, text, top=True):
    """Big readable text on a semi-transparent black bar."""
    h, w = frame.shape[:2]
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale, thickness, line_h, pad = 0.7, 2, 30, 10
    lines = wrap(text, max(20, w // 14))
    box_h = line_h * len(lines) + pad * 2
    y0 = pad if top else h - box_h - pad
    overlay = frame.copy()
    cv2.rectangle(overlay, (0, y0), (w, y0 + box_h), (0, 0, 0), -1)
    cv2.addWeighted(overlay, 0.6, frame, 0.4, 0, frame)
    for i, line in enumerate(lines):
        y = y0 + pad + line_h * (i + 1) - 8
        cv2.putText(frame, line, (pad, y), font, scale, (255, 255, 255), thickness, cv2.LINE_AA)

# === MAIN LOOP ===
print(f"Question: {question}")
print("Generating every 10 seconds, press q to quit.")

last_ask_time = 0
interval = 10  # seconds

while True:
    ret, frame = cap.read()
    if not ret:
        break
    current_frame = frame.copy()

    # Every interval seconds, issue a new ask() if not processing
    now = time.time()
    if now - last_ask_time >= interval and not processing:
        ask()
        last_ask_time = now

    status = "Processing..." if processing else f"Auto-generating every {interval} seconds | q = quit"
    draw_text(frame, status, top=True)
    if response_text:
        draw_text(frame, response_text, top=False)

    cv2.imshow('LLaVA Live', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    # No action on space anymore

cap.release()
cv2.destroyAllWindows()