import uvicorn
from server.core import config


def run():
    uvicorn.run(
        "server.app:app",
        host=config.HOST,
        port=config.PORT,
        reload=config.DEBUG,
    )


if __name__ == "__main__":
    run()
