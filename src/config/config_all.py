import os

# usar este arquivi para a importacao de informacoes sensiveis
class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    DEBUG = os.getenv("DEBUG", "True") == "True"