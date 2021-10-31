from typing import List

from fastapi import APIRouter, Depends
from requests import Session

from src.controllers.users import UsersController
from src.db.base import SessionLocal
from src.schemas.user import User

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[User])
async def get_users(db: Session = Depends(get_db)):
    users = UsersController.get(db)
    return users
