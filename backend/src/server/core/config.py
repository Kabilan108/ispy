"""Config  file for FastAPI server."""

from decouple import Config

MONGO_USER = Config("MONGO_USER", default=None)
MONGO_PASS = Config("MONGO_PASS", default=None)
MONGO_URI = Config("MONGO_URI", default=None)
FASTAPI_PORT = Config("FASTAPI_PORT", default=4000)
