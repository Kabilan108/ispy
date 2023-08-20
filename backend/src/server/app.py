"""FastAPI application instance."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.core import config

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


@app.get("/", tags=["Root"])
async def root() -> dict:
    return {"message": "yooo"}
