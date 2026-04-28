"""This module contains the bachend logic for the main application."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
app = FastAPI()
#CORS (For react)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#database connection
conn =mysql.connector.connect(
    host="localhost",
    user="root",
    password="D2a0y0a5%2026",
    database="fintech_db"
)
print("Connection created")
@app.get("/")
def home():
    """Home endpoint to check if the API is working."""
    return {"message": "Welcome to the Fintech API!"}

@app.get("/transactions")
def get_transactions():
    """Fetch all transactions from the database."""
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    return {"transactions": transactions}
