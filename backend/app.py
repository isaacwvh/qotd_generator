from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  

quotes = [
    "You do not have to see the whole path to take the next step.",
    "Discipline is choosing what you want most over what you want now.",
    "Start before you are ready; clarity comes from doing.",
    "Be proud of how far you have come, and excited for what comes next.",
    # "Your future is built from what you do today, not what you plan tomorrow.",
    # "Courage is not the absence of fear; it is moving forward with it.",
    # "A little progress every day adds up to big change.",
    # "You are allowed to be a work in progress and still be worthy of love.",
    # "Focus on what you can control, and let the rest be noise.",
    # "Make decisions as the person you want to become.",
    # "Imperfection is beauty, madness is genius and it is better to be absolutely ridiculous than absolutely boring.",
    "Without music, life would be a mistake.",
    "without drake, life would be a mistake",
    "Everything you can imagine is real.",
    "Life isn't about finding yourself. Life is about creating yourself",
    "CAREFUL, you might miss it! https://secret-self-ten.vercel.app/ (copy paste in your browser)"
]


@app.get("/quote")
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

@app.get("/")
def home():
    return "Flask backend is running!"

if __name__ == "__main__":
    app.run(debug=True)
