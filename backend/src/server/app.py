from fastapi import FastAPI

# from .routes.route import router as RouteRouter

app = FastAPI()

# app.include_router(ROUTER, tags=[""] prefix="")

@app.get("/", tags=["Root"])
async def root() -> dict:
    return {"message": "yooo"}
