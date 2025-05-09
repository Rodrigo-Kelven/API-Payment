from fastapi import APIRouter, Depends, HTTPException, Request, Response, status, Query
from fastapi_limiter.depends import RateLimiter
from typing import List
from core.config.config import app_logger, limiter

route_based = APIRouter()


@route_based.get(
    path='/test',
    status_code=status.HTTP_200_OK,
    description="Route Home",
    name="Route Name"
)
@limiter.limit("10 per hour")  # 10 requisições por hora
async def routeHome(request: Request):
    app_logger.info(
        msg="Route /test funcionando"
    )
    return {"Hello Word!"}


@route_based.get(
    path="/",
    status_code=status.HTTP_200_OK,
    description="Rota sem limit de requisicoes",
    name="Route no limit request",
    response_description="No Limit Request"
)
@limiter.limit("5 per second;50 per minute")  # 5 requisições por segundo, mas no máximo 50 por minuto
async def index(request: Request):
    return {"msg": "This endpoint has no limits."}

@route_based.get(
    path="/search",
    status_code=status.HTTP_200_OK,
    description="Rota com limit de requisicoes",
    name="Route with limit request",
    response_description="With Limit Request"
)
@limiter.limit("5 per second;50 per minute")  # 5 requisições por segundo, mas no máximo 50 por minuto
async def search_handler(request: Request):
    return {"msg": "This endpoint has a rate limit of 2 requests per 5 seconds."}

@route_based.get(
    path="/upload",
    description="Rota com limit de requisicoes",
    name="Route with limit request",
    response_description="With Limit Request"
)
@limiter.limit("1 per second;50 per minute")  # 1 requisições por segundo, mas no máximo 50 por minuto
async def upload_handler(request: Request):
    return {"msg": "This endpoint has a rate limit of 2 requests per 10 seconds."}


# Simulando uma lista de itens
items = [{"item_id": i, "name": f"Item {i}"} for i in range(1, 101)]  # 100 itens

@route_based.get(
    path="/items/",
    response_model=List[dict],
    description="Rota com pagination",
    name="Route with pagination",
    response_description="With Pagination"
)
async def get_items(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, gt=0)
):
    """
    Retorna uma lista de itens com paginação.
    - **skip**: Número de itens a serem pulados (offset).
    - **limit**: Número máximo de itens a serem retornados.
    """
    return items[skip: skip + limit]