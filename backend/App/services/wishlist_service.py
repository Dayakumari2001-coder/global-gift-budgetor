"""wishlist_service.py - Service to handle wishlist item operations."""
from ..db import get_connection

def add_item(item):
    """Add a wishlist item to the database."""
    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO wishlist (user_id, item_name, foreign_price, currency)
        VALUES (%s, %s, %s, %s)
    """, (item.user_id, item.item_name, item.price, item.currency))

    db.commit()
