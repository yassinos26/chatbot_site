from flask import Flask, render_template, request, jsonify
import google.generativeai as genia

import os
API_KEY = os.getenv("API_KEY")

if API_KEY is None:
    raise ValueError("API_KEY environment variable not set.")

app = Flask(__name__)

API_KEY = "AIzaSyBRJovh1LGCsLN2pH_RYcwWu2itj53UyE8"
genia.configure(api_key=API_KEY)
model = genia.GenerativeModel("gemini-1.5-flash-002")
chat = model.start_chat()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_route():
    data = request.get_json()
    user_input = data.get("message", "")
    if user_input.lower() == "cancel":
        return jsonify({"response": "Session terminée."})
    response = chat.send_message(user_input)
    return jsonify({"response": response.text})

if __name__ == "__main__":
    print("App is running...")
    app.run(debug=True)

