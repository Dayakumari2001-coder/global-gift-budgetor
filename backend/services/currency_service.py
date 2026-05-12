"""currency_service.py - Service to handle currency conversion logic."""
import sqlite3
from db import get_connection
import requests
from core.config import settings

def update_exchange_rates(user_id):
    """Fetch and update exchange rates in the database."""
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT home_currency FROM users WHERE user_id=?",(user_id))
    result=cursor.fetchone()
    if not result:
        print(f"User {user_id} not found.")
        return
    base_currency=result[0]

    # Fetch all unique currencies from the wishlist
    cursor.execute("SELECT DISTINCT currency FROM wishlist WHERE user_id=?",(user_id))
    target_currencies = [row[0] for row in cursor.fetchall()]

    if not target_currencies:
        print("No curencies found in any wishlist.")
        return None

    url = f"{settings.EXCHANGE_RATE_BASE_URL}/latest/{base_currency}"
    response = requests.get(url, timeout=(5, 30))

    if response.status_code !=200:
        print("failed to fetch exchange rates from API.")
        return
    data=response.json()
    rates=data.get("conversion_rates",{})
    last_update=data.get("last_update")

    # Update exchange rates for each currency to base_currency
    for currency in target_currencies:
        if currency != base_currency:
            if currency in rates:
                rate=rates[currency]
                try:
                    cursor.execute("""
                        INSERT INTO exchange_rates (target_currency, rate)
                        VALUES (?, ?)
                        ON CONFLICT (targate_currency) DO UPDATE SET
                        rate = EXCLUDED.rate WHERE user_id=?
                    """, (currency, rate, user_id))
                except sqlite3.Error as e:
                    return f"Error fetching rate for {currency}: {e}"

    db.commit()
    return{
        "status":"success",
        "message":"rates updated successful",
        "last_update": last_update
    }

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
