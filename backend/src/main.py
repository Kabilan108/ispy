import uvicorn
from src.server.core import config

if __name__ == "__main__":
    uvicorn.run("server.app:app", host="0.0.0.0", port=config.PORT, reload=True)
