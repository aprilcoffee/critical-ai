# LLaVA & Python
# Send a local image to LLaVA and print its description.
#
# Install:  pip install ollama
# Pull:     ollama pull llava

from pathlib import Path
import ollama

# Anchor to this script's folder, not where you run python from.
HERE = Path(__file__).parent
image_path = HERE / "images" / "image.jpeg"

# Read the file as bytes. No path guessing, no surprises.
data = image_path.read_bytes()

response = ollama.chat(
    model="llava", #gemma3:4b"
    messages=[{
        "role": "user",
        "content": "Describe this image in detail.",
        "images": [data],
    }],
)

print(response["message"]["content"])
