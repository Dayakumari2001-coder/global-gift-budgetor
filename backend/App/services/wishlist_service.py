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

def update_item(item_id, item):
    """update item details using item_id"""
    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        UPDATE wishlist
        SET item_name=%s, foreign_price=%s, currency=%s
        WHERE id=%s
    """, (item.item_name, item.price, item.currency, item_id))

    db.commit()


def delete_item(item_id):
    """Delete a wishlist item from the database."""
    db = get_connection()
    cursor = db.cursor()

    cursor.execute("DELETE FROM wishlist WHERE id=%s", (item_id,))
    db.commit()
