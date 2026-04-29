"""currency_service.py - Service to handle currency conversion logic."""
from ..db import get_connection

def convert_to_inr():
    """Convert wishlist foreign prices to Indian Rupees using exchange rates."""
    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT SUM(w.foreign_price * e.rate_to_inr)
        FROM wishlist w
        JOIN exchange_rates e ON w.currency = e.currency
    """)

    result = cursor.fetchone()[0]
    return result or 0
