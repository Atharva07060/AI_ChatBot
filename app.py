from flask import Flask, request, jsonify
from chat_model import get_intent

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    intent, confidence = get_intent(user_message)

    # Simple response logic
    if "refund" in user_message.lower():
        response = "I understand you want a refund. Please provide your order ID."
    elif "order" in user_message.lower():
        response = "Sure, I can help track your order. Could you share your order ID?"
    elif "issue" in user_message.lower():
        response = "Sorry to hear that. Can you describe the technical issue in detail?"
    else:
        response = "Thanks for reaching out! How can I assist you today?"

    return jsonify({
        "user_message": user_message,
        "intent": intent,
        "confidence": confidence,
        "bot_response": response
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
