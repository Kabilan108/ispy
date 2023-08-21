"""FastAPI application instance."""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from server.core import config
from server.schema.base import Response

from server.services import openai

# from .routes.route import router as RouteRouter

app = FastAPI()

# add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ORIGINS,
    allow_credentials=config.CREDENTIALS,
    allow_methods=config.METHODS,
    allow_headers=config.HEADERS,
)

# add routers
# app.include_router(ROUTER, tags=[""] prefix="")


@app.get("/", tags=["Root"], response_model=Response)
async def read_root() -> dict:
    return {"success": True, "data": {"message": "yooo"}}


@app.get("/error", response_model=Response)
async def trigger_error():
    raise HTTPException(status_code=400, detail="This is a bad request!")


@app.get("/kaboom", response_model=Response)
async def trigger_kaboom():
    joke = openai.random_joke()
    return {"success": True, "data": {"joke": joke.choices[0].message.content}}
