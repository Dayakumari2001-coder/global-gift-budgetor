"""Database connection"""
import mysql.connector
import os

def get_connection():
    """Create and return a MySQL database connection."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("DATABASE_PASSWORD"),

        database="gift_db"
    )
