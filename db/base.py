from db.base_class import Base
from db.models.user import User
from fastapi import APIRouter
from apis.v1 import route_user,route_login

api_router = APIRouter()
api_router.include_router(route_user.router, prefix="",tags=["users"])
api_router.include_router(route_login.router, prefix="", tags=["login"])