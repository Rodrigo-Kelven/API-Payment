from fastapi import APIRouter, status


route_based = APIRouter()


@route_based.get(
    path='/test',
    status_code=status.HTTP_200_OK,
    description="Route Home",
    name="Route Name"
)
async def routeHome():
    return "Hello Word"