from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from src import models
from src.db.base import SessionLocal
from src.models.user import User


class UsersController:
    def get(self, db: Session) -> List[User]:
        users = db.query(models.User).all()
        print(users)
        return []
