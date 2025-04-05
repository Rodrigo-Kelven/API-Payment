from fastapi import FastAPI
from config.config import lifespan
from routes.all_routes import all_Rotes

app = FastAPI(lifespan=lifespan)

all_Rotes(app)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)