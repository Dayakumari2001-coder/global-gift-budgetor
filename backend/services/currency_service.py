"""currency_service.py - Service to handle currency conversion logic."""
import sqlite3
from backend.db import get_connection
import requests
from core.config import settings


def update_exchange_rates():
    """Cron job triggered:Fetch and update exchange rates in the database ."""
    try:
        url = f"{settings.EXCHANGE_RATE_BASE_URL}/latest/USD"
        response = requests.get(url, timeout=(5, 30))

        if response.status_code !=200:
            print("failed to fetch exchange rates from API.")
            return
        data=response.json()
        rates=data.get("rates",{})

        db = get_connection()
        cursor = db.cursor()
        query="""
            INSERT INTO exchange_rates (base_currency, target_currency, currenct_rate)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE 
            current_rate= VALUES(current_rate) last_updated=NOW();
        """
        # Update exchange rates for each currency to base_currency
        for currency ,rate in rates.items():
            cursor.execute(query, ("USD", currency, rate))

        db.commit()
        cursor.close()
        db.close()
    except sqlite3.Error as e:
        return f"Error fetching rate for {currency}: {e}"

def get_total(wishlist_id, user_id):
    """Calculate the total budget in the specified home currency."""
    db = get_connection()
    cursor = db.cursor()
    try:
        cursor.execute("""
            SELECT SUM(w.foreign_price * e.rate)
            FROM wishlist w
            JOIN exchange_rates e
            ON w.currency = e.target_currency
            WHERE w.wishlist_id, w.user_id= ?, ?
        """, (wishlist_id, user_id))

        row = cursor.fetchone()[0]
        total = row[0] if row  and row[0] is not None else 0
        return {
            "total_budget":total
    }
    except sqlite3.Error as e:
        return f"Database error: {e}"
