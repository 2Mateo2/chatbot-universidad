from flask import Flask, request, jsonify
from flask_cors import CORS
from core.chatbot import get_response

app = Flask(__name__)
CORS(app)

@app.route('/chatbot', methods=['POST'])
def chatbot_response():
    try:
        data = request.get_json()
        user_message = data.get('mensaje')
        if not user_message:
            return jsonify({"error": "No se proporcionó ningún mensaje."}), 400

        response = get_response(user_message)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def run_flask():
    app.run(debug=True, use_reloader=False)
