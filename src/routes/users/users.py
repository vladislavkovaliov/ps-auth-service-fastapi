from typing import List

from fastapi import APIRouter
from src.controllers.users import UsersController
from src.models.user import User

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[User])
async def get_users():
    users = UsersController.get()
    return users
