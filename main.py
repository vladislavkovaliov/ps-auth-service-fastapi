from fastapi import Depends, FastAPI

from src.routes.users import users
from src.routes.user import user


app = FastAPI(dependencies=[])

app.include_router(users.router)
app.include_router(user.router)
