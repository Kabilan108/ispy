"""Route for Speech to Text (STT) and Text to Speech (TTS)"""

from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.services.mongo import MongoDB

router = APIRouter()


@router.get("/")
async def speech():
    """Root route for speech."""
    pass


@router.get("/tts")
async def tts():
    """Text to speech route."""
    pass
