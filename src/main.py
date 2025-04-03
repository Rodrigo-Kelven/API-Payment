import logging
from fastapi import FastAPI
from config.config import LogRequestMiddleware, rate_limit_middleware
from routes.all_routes import all_Rotes


app = FastAPI(
    debug=True,
    title="API Based with FastAPI",
    version="0.0.1",
    summary="Este projeto é uma API RESTful para um sistema base completo."
    "A ideia e criar um pequeno sistema base e usa-lo como base em outros projetos."
)

all_Rotes(app)

# Adiciona o middleware ao FastAPI, verifica requests e responses
app.add_middleware(LogRequestMiddleware)

# funcao para configuracao do middleware
app.middleware("http")(rate_limit_middleware)

# Configure o logging para depuração
logging.basicConfig(level=logging.DEBUG)

