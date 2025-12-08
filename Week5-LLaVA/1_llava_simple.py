from ollama import chat

# Change this to your image absolute path
image_path = "/Users/tcliu/Documents/GitHub/critical-ai/test/llava/myface_2.JPG"
# To use a live URL image instead of a local path, just set 'image_path' to the URL string.

# image_path = "https://example.com/your_image.jpg"



prompt = input("Enter your question about the image: ")

result = chat(
    model='llava',
    messages=[{
        'role': 'user',
        'content': f'{prompt} {image_path}'
    }]
)

print(result['message']['content'])
