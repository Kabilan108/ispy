"""Route for TTS and STT"""

from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.services import MongoDB

router = APIRouter()


@router.get("/tts")
async def tts():
    """Text to speech route."""
    pass
