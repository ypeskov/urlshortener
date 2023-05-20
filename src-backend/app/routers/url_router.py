from typing import Annotated, Union

from fastapi import APIRouter, status
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.routers import url_crud
from ..database import get_db
from .url_schemas import UrlResponse, UrlCreate, ErrorGenerateShortUrl

router = APIRouter(prefix='/urls',
                   tags=['Urls API'])


@router.post("/", response_model=Union[UrlResponse, ErrorGenerateShortUrl])
def create_url(url: UrlCreate, db: Annotated[Session, Depends(get_db)]):
    number_of_attempts = 0
    while True:
        if number_of_attempts > 100:
            return ErrorGenerateShortUrl()
        number_of_attempts += 1
        new_url = url_crud.create_url(db, url)
        if new_url is None:
            continue
        else:
            return new_url