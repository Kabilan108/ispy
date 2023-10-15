# app/schema/base.py

from typing import Optional

from pydantic import BaseModel, Field


class Response(BaseModel):
    """Base response model."""

    message: Optional[str] = Field(None, example="Success")
    data: Optional[dict] = Field(None, example={"message": "yooo"})
    success: bool = Field(..., example=True)
