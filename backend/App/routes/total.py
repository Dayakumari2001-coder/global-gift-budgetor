"""total.py - Route to calculate total budget in INR."""
from fastapi import APIRouter
from ..services.currency_service import get_total  # type: ignore

router = APIRouter()

@router.get("/total/{currency}")
def total(currency: str):
    """Calculate and return the total budget in the specified currency."""
    value = get_total(currency)
    return {"total": round(value, 2), "currency": currency}
