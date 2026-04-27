from ollama import generate

t = input("first prompt:\n")
response = generate(
    model="llama3.2", prompt=t,system="Answer in German")

print(response.response)
#print(response.message)