from typing import List

from fastapi import APIRouter, Depends, HTTPException
from requests import Session

from src.controllers.users import UsersController
from src.db.base import SessionLocal

from src import schemas


STATUS_TEXT_400 = "User not found."
STATUS_TEXT_404 = "User already exists."


router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[],
    responses={
        404: {"description": STATUS_TEXT_404},
        400: {"description": STATUS_TEXT_400},
    }
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[schemas.UserResponse])
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = UsersController.get(db, skip, limit)
    return users


@router.post("/", response_model=schemas.UserResponse)
async def post_users(user: schemas.UserRequest, db: Session = Depends(get_db)):
    name = user.name
    f_user = UsersController.get_user_by_name(db, name)

    if f_user is not None:
        raise HTTPException(status_code=400, detail=STATUS_TEXT_400)
    else:
        new_user = UsersController.insert(db, user)
        return new_user
