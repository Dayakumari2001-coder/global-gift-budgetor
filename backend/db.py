"""Database connection"""
import mysql.connector
from backend.core.config import settings


def get_connection():
    """Create and return a MySQL database connection."""
    return mysql.connector.connect(
        host=settings.DB_HOST,
        user=settings.DB_USER,
        password=settings.DB_PASSWARD,
        database=settings.DB_NAME
    )
