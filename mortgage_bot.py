import openai
import requests
import random
import re
from flask import Flask, request, jsonify
from flask_cors import CORS  # Allows API to be called from different domains
import os  # Secure API Key Storage

app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend requests

# ✅ Store OpenAI API Key Securely (Set this in your environment variables)
openai.api_key = os.getenv("OPENAI_API_KEY", "your_actual_openai_api_key")

# ✅ GPT-4 Chatbot Logic
def mortgage_chatbot(user_id, user_input):
    try:
        gpt_response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a highly knowledgeable mortgage AI assistant helping real estate investors."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=500,
            temperature=0.7
        )
        response_text = gpt_response["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"GPT-4 Error: {e}")
        response_text = "I'm currently unavailable. Please try again later."

    return response_text

# 🚀 Chatbot API Route
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").strip()
    user_id = request.json.get("user_id", "default_user")

    response_text = mortgage_chatbot(user_id, user_input)
    return jsonify({"response": response_text})

# ✅ Run the Flask App
if __name__ == "__main__":
    app.run(port=5000, debug=True)
