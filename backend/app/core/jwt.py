# app/core/jwt.py

from datetime import datetime, timedelta
import jwt

from app.core import config


def create_jwt(data: dict):
    expiration = datetime.utcnow() + timedelta(hours=config.TOKEN_EXPIRE_HOURS)
    return jwt.encode(
        {"exp": expiration, **data}, config.SECRET_KEY, algorithm=config.ALGORITHM
    )


def decode_jwt(token: str):
    try:
        return jwt.decode(token, config.SECRET, algorithms=[config.ALGORITHM])
    except jwt.ExpiredSignatureError:
        return None
