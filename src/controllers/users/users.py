from typing import List, Optional
from sqlalchemy.orm import Session
from src import models, schemas


class UsersController:
    @staticmethod
    def get(db: Session, skip: int = 0, limit: int = 100):
        users = db.query(models.User).offset(skip).limit(limit).all()
        return users

    @staticmethod
    def get_user_by_name(db: Session, name: str) -> Optional[schemas.User]:
        f_user = db.query(models.User).filter_by(name=name).one_or_none()
        return f_user

    @staticmethod
    def insert(db: Session, user: schemas.User) -> schemas.User:
        db_user = models.User(name=user.name)

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

