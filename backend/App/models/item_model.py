"""Pydantic model definitions for items in the global gift budgetor backend."""

from pydantic import BaseModel, Field

class Item(BaseModel):
    """Model representing a gift item with price and currency information."""
    item_name: str = Field(min_length=2)
    price: float = Field(gt=0)
    currency: str
