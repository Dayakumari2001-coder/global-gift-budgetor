"""currency_service.py - Service to handle currency conversion logic."""
import sqlite3
from ..db import get_connection
from forex_python.converter import CurrencyRates

currency_rates = CurrencyRates()

def update_exchange_rates():
    """Fetch and update exchange rates in the database."""
    db = get_connection()
    cursor = db.cursor()

    # Fetch all unique currencies from the wishlist
    cursor.execute("SELECT DISTINCT currency FROM wishlist")
    currencies = [row[0] for row in cursor.fetchall()]
    cursor.execute("SELECT DISTINCT home_currency FROM users")
    home_currencies = [row[0] for row in cursor.fetchall()]

    # Update exchange rates for each currency to home_currency
    for currency in currencies:
        for home_currency in home_currencies:
            if currency != home_currency:
                try:
                    rate = currency_rates.get_rate(currency, home_currency)
                    cursor.execute("""
                        INSERT INTO exchange_rates (from_currency, to_currency, rate, last_updated)
                        VALUES (%s, %s, %s, NOW())
                        ON CONFLICT (from_currency, to_currency) DO UPDATE
                        SET rate = EXCLUDED.rate, last_updated = EXCLUDED.last_updated
                    """, (currency, home_currency, rate))
                except sqlite3.Error as e:
                    return f"Error fetching rate for {currency}: {e}"
                except KeyError as e:
                    return f"Currency not found: {currency} or {home_currency}: {e}"

    db.commit()

def get_total(home_currency):
    """Calculate the total budget in the specified home currency."""
    if not home_currency:
        return "Error: No currency provided."
    try:
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
    except sqlite3.Error as e:
        return f"Database error: {e}"
    db.comit()
