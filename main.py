import uvicorn
from fastapi import FastAPI

from src import models
from src.db.base import database, engine
from src.routes.users import users
from src.routes.user import user


models.Base.metadata.create_all(bind=engine)


app = FastAPI(dependencies=[])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(users.router)
app.include_router(user.router)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)
