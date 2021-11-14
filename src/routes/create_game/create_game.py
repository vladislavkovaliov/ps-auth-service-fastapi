import shutil

from fastapi import APIRouter, UploadFile, File, Form, Depends

from src import schemas
from src.controllers.create_games import CreateGameController
from src.db import get_db
from requests import Session

router = APIRouter(
    prefix="/create-game",
    tags=["game"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=schemas.GameResponse)
async def post_game(title: str = Form(...), sound: str = Form(...), price: str = Form(...), city: str = Form(...),
                    file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_path = 'files/' + f'{file.filename}'
    with open(file_path, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    game = CreateGameController.insert(db, title, sound, price, city, file_path)

    return game
