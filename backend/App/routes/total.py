"""total.py - Route to calculate total budget in INR."""
from fastapi import APIRouter
from ..services.currency_service import get_total
from ..db import get_connection

router = APIRouter()

@router.get("/total/{currency}")
def total(currency: str):
    """Calculate and return the total budget in the specified currency."""
    value = get_total(currency)
    return {"total": round(value, 6), "currency": currency}

@router.get("/rate-time/{currency}")
def rate_time(currency: str):
    """Get the last updated time for exchange rates of the specified currency."""
    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT last_updated 
        FROM exchange_rates
        WHERE to_currency = %s 
        LIMIT 1
    """, (currency,))

    result = cursor.fetchone()
    return {"last_updated": result[0] if result else None}
