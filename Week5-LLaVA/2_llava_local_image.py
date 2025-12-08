from ollama import chat
import os

# Change this to your image absolute path
image_path = "/Users/tcliu/Documents/GitHub/critical-ai/test/llava/myface_2.JPG"
image_path = os.path.abspath(image_path)

prompt = input("Enter your question about the image: ")

result = chat(
    model='llava',
    messages=[{
        'role': 'user',
        'content': f'{prompt} {image_path}'
    }]
)

print(result['message']['content'])
