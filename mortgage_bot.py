import requests
import random
import re
import speech_recognition as sr
from flask import Flask, request, jsonify

app = Flask(__name__)

# 🎯 AI Mortgage Chatbot - Fully Contextualized, Adaptive & Smart
conversation_state = {}

# 🌍 Voice AI - Speech Processing
recognizer = sr.Recognizer()


# 📌 Enhanced AI Response Variations with Real-Time Context Awareness
response_variations = {
    "loan_officer_request": [
        "I appreciate you reaching out! I'll connect you with a Loan Officer. Would you prefer a phone call, email, or text?",
        "One of our experts will reach out. What’s the best way to contact you – phone, email, or text?",
        "I can arrange for a Loan Officer to contact you ASAP. What’s your preferred method?"
    ],
    "fix_and_refinance": [
        "Great strategy! Here’s how **Fix & Refinance** works:\n"
        "1️⃣ **Step 1:** Short-term **Fix & Flip Loan** to acquire and renovate your property.\n"
        "2️⃣ **Step 2:** **DSCR Loan (30-year fixed)** to refinance and secure long-term rental income.\n"
        "3️⃣ **Step 3:** Pull equity and scale your investments! 🚀\n"
        "Would you like to calculate your potential refinance equity?",
        "Fix & Flip + DSCR Refinance is the ultimate investor strategy.\n"
        "✅ **Fast Fix & Flip Loans** – Close in **5-10 days**\n"
        "✅ **DSCR Refinance** – No income verification, qualify based on rental income\n"
        "✅ **Maximize Leverage** – Get up to 80% LTV\n"
        "Want a detailed breakdown for your deal?"
    ],
    "dscr": [
        "DSCR Loans qualify you based on **rental income, not personal income.**\n"
        "📌 **No W-2s, no tax returns** needed!\n"
        "📌 **Max LTV:** 80%\n"
        "📌 **Loan Amounts:** $100K - $75M\n"
        "📌 **1.0+ DSCR required (rental income covers mortgage payments)**\n"
        "Would you like to calculate your DSCR ratio?",
        "A DSCR Loan lets you finance rental properties **without proving personal income.**\n"
        "🔥 **Perfect for landlords & Airbnb investors**\n"
        "📈 **Based on property cash flow, not credit score!**\n"
        "Want me to estimate your DSCR qualification?"
    ],
    "apply": [
        "Applying is easy! 🚀\n"
        "📌 Visit our secure portal: [INSERT APPLICATION LINK]\n"
        "📌 Takes **10 minutes** to complete\n"
        "📌 Get pre-approved within 24 hours\n"
        "Want me to send you the link via email or text?",
        "To apply for financing, simply visit **[INSERT LOAN APPLICATION LINK]**.\n"
        "Need help filling it out? I can walk you through the process."
    ],
    "loan_amounts": [
        "We fund loans between **$100,000 - $100,000,000 for CRE** and **$100,000 - $75,000,000 for REI**.\n"
        "Would you like to see what financing options fit your deal?",
        "Our funding range covers all types of real estate investments!\n"
        "Do you need a short-term or long-term financing option?"
    ],
    "property_location": [
        "We lend **nationwide for non-owner occupied properties**.\n"
        "For **owner-occupied**, we currently serve **California & Florida**.\n"
        "Which state is your project located in?",
        "Our lending network covers all **50 states for investment real estate**.\n"
        "Let me know where your property is located so I can match you with a loan program."
    ],
    "follow_up_yes": [
        "Excellent! Let's get started.\n"
        "What details do you need help with first – loan amounts, interest rates, or qualification steps?",
        "Glad to hear that! Tell me, are you looking for a same-day consultation with a Loan Officer?"
    ],
    "default": [
        "I specialize in real estate investment financing, nationwide lending, and strategic loan structuring. "
        "How can I assist you today?",
        "APR Capital Mortgage helps investors **finance Fix & Flip, DSCR, and Commercial deals**. "
        "Tell me more about your project, and I'll guide you."
    ]
}

# ✨ AI Mortgage Chatbot Logic with Contextual NLP Responses & Smart Reply Generation
def mortgage_chatbot(user_id, user_input):
    user_input = user_input.lower().strip()

    if user_id not in conversation_state:
        conversation_state[user_id] = {}

    # Detect Loan Officer Request & Follow-Up
    if "loan officer" in user_input or "speak to someone" in user_input:
        conversation_state[user_id]["awaiting_contact_method"] = True
        return random.choice(response_variations["loan_officer_request"])

    # Fix & Refinance Path
    elif "fix and refinance" in user_input or "brrr" in user_input:
        conversation_state[user_id]["awaiting_refinance_details"] = True
        return random.choice(response_variations["fix_and_refinance"])

    # DSCR-Specific Expanded Intelligence
    elif "dscr" in user_input:
        return random.choice(response_variations["dscr"])

    # Loan Amounts
    elif "loan amount" in user_input or "how much can i get" in user_input:
        return random.choice(response_variations["loan_amounts"])

    # Property Location
    elif "where do you lend" in user_input or "which states" in user_input:
        return random.choice(response_variations["property_location"])

    # Application Request
    elif "apply" in user_input or "how do i start" in user_input:
        return random.choice(response_variations["apply"])

    # Confirm Yes Response for Guidance
    elif user_input in ["yes", "sure", "show me how", "let’s do it", "go ahead"]:
        return random.choice(response_variations["follow_up_yes"])

    # Default Catch-All (Varied)
    else:
        return random.choice(response_variations["default"])

# 🚀 Chatbot Route
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").strip()
    user_id = request.json.get("user_id", "default_user")

    response_text = mortgage_chatbot(user_id, user_input)
    return jsonify({"response": response_text})

# 🎙️ Voice AI Processing Route
@app.route("/voice_chat", methods=["POST"])
def voice_chat():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for voice input...")
        try:
            audio = recognizer.listen(source)
            user_input = recognizer.recognize_google(audio)
            response_text = mortgage_chatbot("voice_user", user_input)

            return jsonify({"response": response_text})
        except sr.UnknownValueError:
            return jsonify({"response": "Sorry, I couldn't understand that. Can you repeat?"})
        except sr.RequestError:
            return jsonify({"response": "Speech recognition service is unavailable at the moment."})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
