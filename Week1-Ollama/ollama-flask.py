from flask import Flask, request
from ollama import chat

app = Flask(__name__)

SYSTEM_PROMPT = "Answer clearly and cleanly."
messages = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form.get("prompt", "").strip()

        if prompt:
            request_messages = [
                {"role": "system", "content": SYSTEM_PROMPT},
                *messages,
                {"role": "user", "content": prompt},
            ]
            response = chat(model="llama3.2", messages=request_messages)
            reply = response["message"]["content"]

            messages.append({"role": "user", "content": prompt})
            messages.append({"role": "assistant", "content": reply})

    html = "<h1>Ollama Chat</h1>"
    html += (
        "<form method='post'>"
        "<input name='prompt' autofocus>"
        "<button type='submit'>Send</button>"
        "</form><hr>"
    )

    for m in messages:
        role = "You" if m["role"] == "user" else "Assistant"
        html += f"<p><b>{role}:</b> {m['content']}</p>"

    return html


if __name__ == "__main__":
    app.run(debug=True, port=5000)
