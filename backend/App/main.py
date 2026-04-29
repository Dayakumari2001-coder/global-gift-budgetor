"""This module contains the backend logic for the main application."""
# Question: Setup FastAPI main app

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import wishlist, total

app = FastAPI()

# CORS (For react)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(wishlist.router)
app.include_router(total.router)
