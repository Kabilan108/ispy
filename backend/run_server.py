import uvicorn
from app.core import config


def run():
    uvicorn.run(
        "app.main:app",
        host=config.HOST,
        port=config.PORT,
        reload=config.DEBUG,
    )


if __name__ == "__main__":
    run()
