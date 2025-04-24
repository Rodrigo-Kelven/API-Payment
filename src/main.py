from fastapi import FastAPI, Request
from core.config.config_db import Base_auth, engine_auth
from routes.all_routes import all_Rotes
from core.auth.auth import ExceptionHandlingMiddleware
from core.config.config import LogRequestMiddleware
from core.config.config import config_CORS
from core.config.config_db import engine_auth, Base_auth
from core.config.config import  db_logger
from core.routes.all_routes import all_routes



app = FastAPI(
    title="API Library with FastAPI",
    debug=True,
    summary="Api Library",
    version="1.1.12",
    description="A Api Library é uma API Library projetada para facilitar a integração de diferentes serviços e plataformas," \
                "permitindo que desenvolvedores criem soluções robustas e escaláveis. Com uma arquitetura modular e flexível," \
                "a Api Library oferece uma ampla gama de funcionalidades para gerenciar dados, realizar autenticação, processar pagamentos e muito mais."
)

# Adiciona as rotas
all_Rotes(app)
all_routes(app)

@app.on_event("startup")
async def startup_event():
    try:
        # Criação das tabelas no banco de dados de usuários
        async with engine_auth.begin() as conn:
            await conn.run_sync(Base_auth.metadata.create_all)
            db_logger.info("Tabela UserDB criada com sucesso.")

    except Exception as e:
        db_logger.error(f"Erro ao criar tabelas: {str(e)}.")


@app.on_event("shutdown")
async def shutdown_event():
    await engine_auth.dispose()
    db_logger.info("Conexões com os bancos de dados encerradas.")

# Adiciona o middleware ao FastAPI
app.add_middleware(LogRequestMiddleware)

# Adiciona o middleware de tratamento de exceções
app.add_middleware(ExceptionHandlingMiddleware)

# Configuração de CORS
config_CORS(app)


