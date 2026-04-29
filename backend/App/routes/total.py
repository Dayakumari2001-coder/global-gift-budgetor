"""total.py - Route to calculate total budget in INR."""
from fastapi import APIRouter
from ..services.currency_service import convert_to_inr

router = APIRouter()

@router.get("/total")
def total():
    """Calculate and return the total budget in INR."""
    total_value = convert_to_inr()
    return {"total_inr": round(total_value, 2)}
