from ollama import chat

SYSTEM_PROMPT = "Answer clearly and cleanly, with short sentences, no list, and no extra commentary. Answer in German"
messages = []

while True:
    prompt = input("You: ").strip()

    # *messages unpacks all previous chat items into this new list.
    request_messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        *messages,
        {"role": "user", "content": prompt},
    ]
    print("Assistant: ", end="", flush=True)

    reply = ""
    for chunk in chat(model="llama3.2", messages=request_messages, stream=True):
        text = chunk["message"]["content"]
        reply += text
        print(text, end="", flush=True)
    print()

    messages.append({"role": "user", "content": prompt})
    messages.append({"role": "assistant", "content": reply})