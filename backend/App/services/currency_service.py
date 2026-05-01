"""currency_service.py - Service to handle currency conversion logic."""
from ..db import get_connection
from forex_python.converter import CurrencyRates

currency_rates = CurrencyRates()

def get_total(home_currency):
    """Calculate the total budget in the specified home currency."""
    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT SUM(w.foreign_price * e.rate)
        FROM wishlist w
        JOIN exchange_rates e
        ON w.currency = e.from_currency
        WHERE e.to_currency = %s
    """, (home_currency,))

    row = cursor.fetchone()[0]
    result=row if row is not None else 0
    return result or 0
