from fastapi import FastAPI
from config.config import lifespan
from routes.all_routes import all_Rotes

app = FastAPI(
    lifespan=lifespan,
    debug=True,
    title="API Based with FastAPI",
    description="API Based é um projeto open source." \
    "Baseado na ideia de facilitar a crição de apis do absoluto," \
    "este projeto é uma ótima opção para os que se perguntem do que é composta uma" \
    "api excelente em termos de seguranca, performance e escalabilidade/flexibilidade.",
    version="0.0.6"
    )

all_Rotes(app)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)