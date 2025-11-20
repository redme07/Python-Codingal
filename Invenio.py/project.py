from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key="your_api_key_is_here")

@app.route("/ask", methods=["POST","GET"])

def ask():
    if request.method == "POST":
        data = request.json
        prompt = data["prompt"]

        response = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = [{"role": "user","content": prompt}]
        )
        ai_reply = response.choices[0].message["content"]

    
        return jsonify({"reply": ai_reply})
    return "API IS RUNNING"
if __name__ == "__main__":
    app.run(debug=True)