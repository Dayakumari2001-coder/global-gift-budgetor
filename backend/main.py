"""This module contains the backend logic for the main application."""
# Question: Setup FastAPI main app

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from services.currency_service import get_total
from routes import wishlist, total

app = FastAPI()

@app.get("/")
def greet():
    """Greet the user."""
    return "Welcome to the Global Gift Budgetor!"

# CORS (For react)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # Your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(wishlist.router)
app.include_router(total.router)

class TotalRequest(BaseModel):
    """Request model for total calculation."""
    home_currency: str

@app.post("/get-total")
def handle_get_total(data: TotalRequest):
    """Handle POST request to calculate total budget."""
    if not data.home_currency:
        raise HTTPException(status_code=400, detail="Please provide a home currency")

    try:
        result = get_total(data.home_currency)
        return {"total": result}
    except ValueError as exc:
        raise HTTPException(status_code=500, detail=str(exc))from exc
