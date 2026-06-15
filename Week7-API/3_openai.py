# ===============================================================
# 3 — CHATGPT / OPENAI  (a paid key)
# ===============================================================
# Exactly the same shape again. The only real differences from
# Gemini are the address, how the key is attached, and where the
# answer sits in the JSON. This one costs a tiny amount per request.
# (The "Codex" coding models live behind this same API — you just
#  change the "model" name below.)
#
# get a key:  https://platform.openai.com/api-keys
# docs:       https://platform.openai.com/docs/api-reference/chat
#
# pip install requests python-dotenv

import os
import requests
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("OPENAI_API_KEY")

# 1. the address
url = "https://api.openai.com/v1/chat/completions"

# 2. the request
#    here the key goes in an "Authorization" header as "Bearer <key>"
headers = {"Authorization": f"Bearer {key}"}
data = {
    "model": "gpt-4o-mini",     # swap for another model, e.g. a Codex model
    "messages": [
        {"role": "user", "content": "Explain what an API is in one sentence."}
    ],
}

# 3. send it and wait
response = requests.post(url, headers=headers, json=data)

# 4. read the answer
answer = response.json()
print(answer["choices"][0]["message"]["content"])
