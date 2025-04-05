docker run --name my-redis-server -p 6379:6379 -d redis redis-server --loglevel warning
fastapi dev main.py --reload --port 8000
