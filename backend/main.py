from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
import os

from .routers import tournament
from .dependencies import init_db

app = FastAPI(title="Badminton Tournament Hub")

origins = os.getenv("ALLOWED_ORIGINS", "").split(",")  # Ensure ALLOWED_ORIGINS is set correctly

if not origins or origins == [""]:
    raise RuntimeError("ALLOWED_ORIGINS environment variable must be set to specific domains and not empty for production")

app.add_middleware(GZipMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Restrict methods
    allow_headers=["Content-Type", "Authorization"],
)

@app.on_event("startup")
async def on_startup():
    """
    Startup event to initialize database connection.
    """
    await init_db()

# Include routers
app.include_router(tournament.router)
# Add more routers for auth and user here