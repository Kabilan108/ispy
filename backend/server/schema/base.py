"""Base models for API responses."""

from pydantic import BaseModel


class Response(BaseModel):
    success: bool
    data: dict = None
    error: str = None
