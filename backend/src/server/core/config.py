"""config  file for FastAPI server."""

from decouple import config
import os

MONGO_USER = config(
    "MONGO_USER",
    default=None,
)
MONGO_PASS = config(
    "MONGO_PASS",
    default=None,
)
MONGO_URI = config(
    "MONGO_URI",
    default=None,
)
PORT = config(
    "FASTAPI_PORT",
    default=4000,
    cast=int,
)
HOST = config(
    "FASTAPI_HOST",
    default="0.0.0.0",
)
DEBUG = config(
    "DEBUG",
    default=False,
    cast=bool,
)
