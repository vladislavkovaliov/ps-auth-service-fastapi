from typing import Optional

from fastapi import Form
from pydantic import BaseModel


class Game(BaseModel):
    title: str
    sound: str
    price: str
    city: str
    file_url: Optional[str]


class GameRequest(Game):
    title: str = Form(...)
    sound: str = Form(...)
    price: str = Form(...)
    city: str = Form(...)


class GameResponse(Game):
    id: Optional[int]

    class Config:
        orm_mode = True
