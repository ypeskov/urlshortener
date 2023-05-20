from pprint import pprint
from typing import Annotated, Union

from fastapi import APIRouter, Request
from fastapi import Depends
from sqlalchemy.orm import Session

from app.routers import url_crud
from ..database import get_db
from .url_schemas import UrlResponse, UrlCreate, ErrorGenerateShortUrl

router = APIRouter(prefix='/urls',
                   tags=['Urls API'])


@router.post("/", response_model=Union[UrlResponse, ErrorGenerateShortUrl])
def create_url(url: UrlCreate,
               db: Annotated[Session, Depends(get_db)],
               r: Request):
    number_of_attempts = 0
    while True:
        # try 100 times to get unique ID otherwise sorry
        if number_of_attempts >= 100:
            return ErrorGenerateShortUrl()
        number_of_attempts += 1
        new_url = url_crud.create_url(db, url)
        if new_url is None:
            continue
        else:
            break

    new_url.short_url = f"{r.url.scheme}://{r.url.hostname}:{str(r.url.port)}/{new_url.short_url_path}"

    return new_url