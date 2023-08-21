"""config  file for FastAPI server."""

from decouple import config
import os

MONGO_USER = config("MONGO_USER", default=None)
MONGO_PASS = config("MONGO_PASS", default=None)
MONGO_URI = config("MONGO_URI", default=None).format(user=MONGO_USER, pwd=MONGO_PASS)
MONGO_DB = config("MONGO_DB", default="ispy")

PORT = config("FASTAPI_PORT", default=4000, cast=int)
HOST = config("FASTAPI_HOST", default="0.0.0.0")
DEBUG = config("DEBUG", default=False, cast=bool)

ORIGINS = config(
    "ORIGINS", default="*", cast=lambda v: [s.strip() for s in v.split(",")]
)
CREDENTIALS = config("CREDENTIALS", default=True, cast=bool)
METHODS = config(
    "METHODS", default="*", cast=lambda v: [s.strip() for s in v.split(",")]
)
HEADERS = config(
    "HEADERS", default="*", cast=lambda v: [s.strip() for s in v.split(",")]
)

OPENAI_API_KEY = config("OPENAI_API_KEY", default=None)
