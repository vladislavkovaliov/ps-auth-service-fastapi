from fastapi import APIRouter
from src.controllers.user import UserController
from src.models.user import User


router = APIRouter(
    prefix="/user",
    tags=["user"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=User)
async def get_user():
    user = UserController.get()
    return user
