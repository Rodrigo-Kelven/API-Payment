from fastapi import APIRouter


route_based = APIRouter()


@route_based.get(
    path='/test'
)
async def routeTest():
    return "Hello Word"