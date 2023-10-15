# app/core/config.py

from decouple import config
import os


PROJECT_NAME = config("_NAME", default="iSpy")
PROJECT_DESC = config(
    "_DESC",
    default="Welcome to iSpy. Your assistant for taking notes and summarizing meetings.",
)
PROJECT_VERSION = config("_VERSION", default="0.1.0")

SECRET_KEY = config("SECRET_KEY")
ALGORITHM = config("ALGORITHM")
TOKEN_EXPIRE_HOURS = config("TOKEN_EXPIRE_HOURS", cast=int)

FASTAPI_URL = config("FASTAPI_URL")
FASTAPI_PORT = config("FASTAPI_PORT", cast=int)
FASTAPI_HOST = config("FASTAPI_HOST")
FASTAPI_RELOAD = config("FASTAPI_RELOAD", cast=bool)

ORIGINS = config("ORIGINS").split(", ")
CREDENTIALS = config("CREDENTIALS", cast=bool)
METHODS = config("METHODS").split(", ")
HEADERS = config("HEADERS").split(", ")

OPENAI_API_KEY = config("OPENAI_API_KEY")
HELICONE_API_KEY = config("HELICONE_API_KEY")
