from typing import List, Optional
from sqlalchemy.orm import Session
from src import models, schemas


class CreateGameController:
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
