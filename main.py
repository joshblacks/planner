# api/index.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Meal Planner API!"})

# Create a handler function for Vercel
def handler(event, context):
    return app(event, context)