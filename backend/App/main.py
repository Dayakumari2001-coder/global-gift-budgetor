"""This module contains the backend logic for the main application."""
# Question: Setup FastAPI main app

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from flask import jsonify, request

from backend.App.services.currency_service import get_total
from .routes import wishlist, total

app = FastAPI()

@app.get("/")
def greet():
    """Greet the user."""
    return "Welcome to the Global Gift Budgetor!"

# CORS (For react)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(wishlist.router)
app.include_router(total.router)

@app.route('/get-total', methods=['POST'])
def handle_get_total():
    """Handle POST request to calculate total budget."""
    data = request.json()
    home_currency = data.get("home_currency")

    #PUT VALIDATION HERE
    if not home_currency:
        #RETURN 400 BECAUSE THE USER DIDN,T PROVIDE REQUIRED INPUT
        return jsonify({"error": "Please provide a home currency"}),400
    try:
        result = get_total(home_currency)
        return jsonify({"total": result})
    except ValueError as e:
        return jsonify({"error": str(e)}),500
