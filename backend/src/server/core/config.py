"""Config  file for FastAPI server."""

from decouple import Config

MONGO_USER = Config("MONGO_USER", default=None)
MONGO_PASS = Config("MONGO_PASS", default=None)
MONGO_URI = Config("MONGO_URI", default=None)
PORT = Config("FASTAPI_PORT", default=4000)
HOST = Config("FASTAPI_HOST", default="0.0.0.0")
DEBUG = Config("DEBUG", default=False, cast=bool)
