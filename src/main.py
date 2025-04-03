from fastapi import FastAPI

from routes.all_routes import all_Rotes

app = FastAPI()

all_Rotes(app)
