from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  

quotes = [
    "Talk is cheap. Show me the code.",
    "Simplicity is the soul of efficiency.",
    "Debugging is twice as hard as writing the code.",
    "Make it work, make it right, make it fast."
]

@app.get("/quote")
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

@app.get("/")
def home():
    return "Flask backend is running!"

if __name__ == "__main__":
    app.run(debug=True)
