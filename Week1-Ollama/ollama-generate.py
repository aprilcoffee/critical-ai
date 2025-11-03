from ollama import generate

t = input("first prompt:\n")
response = generate(model="llama3.2", prompt=t)
print(response.response)
#print(response.message)