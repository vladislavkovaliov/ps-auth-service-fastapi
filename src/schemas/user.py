from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    name: str


class UserResponse(User):
    id: Optional[int]

    class Config:
        orm_mode = True


class UserRequest(User):
    pass

