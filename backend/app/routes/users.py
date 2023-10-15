"""Route for Managing Users"""

from fastapi import APIRouter

from app.services.mongo import MongoDB

router = APIRouter()


@router.get("/")
async def users():
    """Root route for users."""
    pass
