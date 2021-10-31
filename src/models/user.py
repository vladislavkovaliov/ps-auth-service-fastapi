from sqlalchemy import Column, Integer, String

from src.db.base import Base


class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
