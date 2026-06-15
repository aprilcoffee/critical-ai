# ===============================================================
# 1 — OLLAMA  (start here: an API on YOUR OWN computer, no key)
# ===============================================================
# An "API" is just an address you send a request to, and it sends
# an answer back. Usually that address lives far away on a company
# server. Ollama puts the same thing on your laptop: the address is
# "localhost" (= this computer). Same idea, no key, no internet, free.
#
# install Ollama:  https://ollama.com
# docs:            https://github.com/ollama/ollama/blob/main/docs/api.md
# first run once in a terminal:  ollama pull gemma3
#
# pip install requests

import requests

# 1. the address we send our request to (the "endpoint")
#    11434 is the door number Ollama listens on, on your machine.
url = "http://localhost:11434/api/chat"

# 2. the request: which model, and what we want to say to it
data = {
    "model": "gemma3:4b",          # swap for any model you pulled
    "messages": [
        {"role": "user", "content": "Explain what an API is in one sentence."}
    ],
    "stream": False,            # give the whole answer at once
}

# 3. send it and wait for the answer
response = requests.post(url, json=data)

# 4. read the answer (it comes back as structured data = JSON)
answer = response.json()
print(answer)
print(answer["message"]["content"])

