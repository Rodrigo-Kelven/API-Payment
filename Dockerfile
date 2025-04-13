# Use a imagem oficial do Python como base
FROM python:3.11-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /src

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY src/requirements.txt .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação para o diretório de trabalho
COPY ./src /src

# Expõe a porta 8000
EXPOSE 8000

# Define o comando padrão para executar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]