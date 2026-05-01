"""Database connection"""
import mysql.connector

def get_connection():
    """Create and return a MySQL database connection."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="D2a0y0a5%2026",
        database="gift_db"
    )
