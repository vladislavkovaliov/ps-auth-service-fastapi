import shutil

from typing import List
from fastapi import APIRouter, UploadFile, File, Form, Depends, status
from requests import Session

from src import schemas
from src.controllers.games.games import GamesController
from src.db import get_db

STATUS_TEXT_400 = "Game not found."
STATUS_TEXT_404 = "Game already exists."


router = APIRouter(
    prefix='/games',
    tags=['games'],
    dependencies=[],
    responses={
        404: {"description": STATUS_TEXT_404},
        400: {"description": STATUS_TEXT_400},
    }
)


@router.get("/", response_model=List[schemas.GameResponse])
async def get_games(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    games = GamesController.get(db, skip, limit)

    return games


@router.get("/{game_id}", response_model=schemas.GameResponse)
async def get_game(game_id: int, db: Session = Depends(get_db)):
    game = GamesController.get_game_by_id(db, game_id)
    return game


@router.post("/", response_model=schemas.GameResponse)
async def post_game(title: str = Form(...), sound: str = Form(...), price: str = Form(...), city: str = Form(...),
                    file: UploadFile = File(None), db: Session = Depends(get_db)):
    file_path = None
    if file is not None:
        file_path = 'files/' + f'{file.filename}'
        with open(file_path, 'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)

    game = GamesController.insert(db, title, sound, price, city, file_path)

    return game


@router.delete("/{game_id}")
async def delete_game(game_id: int, db: Session = Depends(get_db)):
    f_game = GamesController.get_game_by_id(db, game_id)
    if f_game is None:
        return status.HTTP_404_NOT_FOUND

    GamesController.remove(db, game_id)

    return status.HTTP_204_NO_CONTENT
