from ollama import generate

# Change this to your image absolute path
image_path = r"/Users/tcliu/Documents/GitHub/critical-ai/Week5-LLaVA/myface_2.JPG"
image_path = r"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages.hindustantimes.com%2Fimg%2F2021%2F12%2F26%2F1600x900%2F2019-12-26T043808Z_1_LYNXMPEFBP044_RTROPTP_4_INDIANOCEAN-TSUNAMI-FILE-1920x1284_1640479059650_1640479137048.jpg"

prompt = input("Enter your question about the image: ")

result = generate(
    model='llava',
    prompt= f'{prompt} {image_path}'
)

print(result.response)
