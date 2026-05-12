"""wishlist.py - Route to add items to the wishlist."""
from fastapi import APIRouter
from models.item_model import Item
from services.wishlist_service import add_item, update_item, delete_item
from db import get_connection

router = APIRouter()

@router.post("/add-item")
def add(item: Item):
    """Add an item to the wishlist."""
    add_item(item)
    return {"message": "Item added"}

@router.put("/edit-item/{item_id}")
def edit_item(item_id: int, item: Item):
    """Edit an existing item in the wishlist."""
    update_item(item_id, item)
    return {"message": "Item updated"}

@router.delete("/delete-item/{item_id}")
def remove_item(item_id: int):
    """Delete an item from the wishlist."""
    delete_item(item_id)
    return {"message": "Item deleted"}

@router.get("/items")
def get_items():
    """Fetch all items from the wishlist."""
    db = get_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM wishlist")
    return cursor.fetchall()
