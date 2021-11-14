from sqlalchemy import Column, Integer, String, BLOB

from src.db.base import Base


class Game(Base):
    __tablename__ = "Games"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=False, nullable=False)
    sound = Column(String, unique=False, nullable=False)
    price = Column(String, unique=False, nullable=False)
    city = Column(String, unique=False, nullable=False)
    file_url = Column(String, unique=False, nullable=True)
