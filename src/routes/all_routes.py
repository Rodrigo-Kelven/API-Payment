from fastapi import APIRouter

from routes.routes import route_based

routes_all = APIRouter()

def all_Rotes(app):
    app.include_router(route_based)