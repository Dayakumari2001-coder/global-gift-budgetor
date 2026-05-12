"""total.py - Route to calculate total budget and get last updated time for exchange rates."""
from fastapi import APIRouter, HTTPException
from services.currency_service import get_total
from db import get_connection

router = APIRouter()

@router.get("/total/{wishlist_id}/{user_id}")
def total(wishlist_id: int, user_id: int):
    """Calculate and return the total budget in the specified currency."""

    db = get_connection()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT home_currency FROM users WHERE user_id=?",(user_id))
        result=cursor.fetchone()
        if not result:
            raise HTTPException(status_code=404, detail=f"User {user_id} not found.")
        home_currency=result[0]

        value = get_total(wishlist_id, user_id)
        return {"total": round(value, 6), "currency": home_currency}
    finally:
        cursor.close()
        db.close()
