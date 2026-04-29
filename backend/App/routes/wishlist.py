"""wishlist.py - Route to add items to the wishlist."""
from fastapi import APIRouter
from ..models.item_model import Item
from ..services.wishlist_service import add_item  # type: ignore

router = APIRouter()

@router.post("/add-item")
def add(item: Item):
    """Add an item to the wishlist."""
    add_item(item)
    return {"message": "Item added"}
