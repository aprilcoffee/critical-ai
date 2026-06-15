# ===============================================================
# 4 — STABILITY AI / DREAMSTUDIO  (the answer is an IMAGE, not text)
# ===============================================================
# Same pattern one last time — but the answer that comes back is not
# words, it is the raw bytes of a PNG file. So instead of printing it,
# we save it to disk. Not every API answers with text.
#
# get a key:  https://platform.stability.ai/account/keys
# docs:       https://platform.stability.ai/docs/api-reference
# (DreamStudio is the website; this is the same Stability behind it.)
#
# pip install requests python-dotenv

import os
import requests
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("STABILITY_API_KEY")

# 1. the address
url = "https://api.stability.ai/v2beta/stable-image/generate/core"

# 2. the request
#    "accept: image/*" tells the server we want an image back
headers = {"Authorization": f"Bearer {key}", "Accept": "image/*"}
data = {
    "prompt": "a giraffe made of static, on a blue background",
    "output_format": "png",
}

# 3. send it and wait
response = requests.post(url, headers=headers, files={"none": ""}, data=data)

# 4. the answer is image bytes -> write them straight into a file
with open("output.png", "wb") as f:
    f.write(response.content)

print("saved output.png")
