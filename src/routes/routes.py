from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from fastapi_limiter.depends import RateLimiter

from config.config import lifespan

route_based = APIRouter()


@route_based.get(
    path='/test',
    status_code=status.HTTP_200_OK,
    description="Route Home",
    name="Route Name"
)
async def routeHome():
    return {"Hello Word"}


@route_based.get(
    path="/",
    status_code=status.HTTP_200_OK,
    description="Rota sem limit de requisicoes",
    name="Route no limit request",
    response_description="No Limit Request"
)
async def index():
    return {"msg": "This endpoint has no limits."}

@route_based.get(
    path="/search",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(RateLimiter(times=2, seconds=5))],
    description="Rota com limit de requisicoes",
    name="Route with limit request",
    response_description="With Limit Request"
)
async def search_handler():
    return {"msg": "This endpoint has a rate limit of 2 requests per 5 seconds."}

@route_based.get(
    path="/upload",
    dependencies=[Depends(RateLimiter(times=3, seconds=10))],
    description="Rota com limit de requisicoes",
    name="Route with limit request",
    response_description="With Limit Request"
)
async def upload_handler():
    return {"msg": "This endpoint has a rate limit of 2 requests per 10 seconds."}
