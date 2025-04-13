from fastapi import FastAPI
from config.config import  cors
from routes.all_routes import all_Rotes

from core.config.config_db import Base, engine
from core.routes.all_routes import all_routes
from core.auth.auth import *
from core.config.config import *


app = FastAPI(
    debug=True,
    title="API Based with FastAPI",
    description="API Based é um projeto open source." \
    "Baseado na ideia de facilitar a crição de apis do absoluto," \
    "este projeto é uma ótima opção para os que se perguntem do que é composta uma" \
    "api excelente em termos de seguranca, performance e escalabilidade/flexibilidade.",
    version="0.1.0"
    )


# inicia todas as rotas implementadas nesta api
all_Rotes(app)
# incia as rotas de authenticacao
all_routes(app)

# tem que ficar no main porque ao ser iniciado, as tabelas no db seram criadas imediatamente
print("Criando tabelas no banco de dados...")
Base.metadata.create_all(bind=engine)
print("Tabelas criadas.")


# Adiciona o middleware ao FastAPI
app.add_middleware(LogRequestMiddleware)

# Adiciona o middleware de tratamento de exceções
app.add_middleware(ExceptionHandlingMiddleware)

# funcao CORS da api de OAthu2
config_CORS(app)

# funcao CORS da api Based
cors(app)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)