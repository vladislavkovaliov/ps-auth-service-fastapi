from typing import Optional

from sqlalchemy.orm import Session

from src import models, schemas


class GamesController:
    @staticmethod
    def get(db: Session, skip: int = 0, limit: int = 0):
        games = db.query(models.Game).offset(skip).limit(limit).all()
        return games

    @staticmethod
    def get_game_by_id(db: Session, game_id: int) -> Optional[schemas.Game]:
        f_game = db.query(models.Game).filter_by(id=game_id).one_or_none()
        return f_game

    @staticmethod
    def insert(db: Session, title: str, sound: str, price: str, city: str, file_path: str):
        db_game = models.Game(
            title=title,
            sound=sound,
            city=city,
            price=price,
            file_url=file_path,
        )

        db.add(db_game)
        db.commit()
        db.refresh(db_game)

        return db_game

    @staticmethod
    def remove(db: Session, game_id: int):
        f_game = db.query(models.Game).filter_by(id=game_id).one_or_none()
        if f_game is not None:
            r_game = db.query(models.Game).filter_by(id=game_id).delete()
            db.commit()
