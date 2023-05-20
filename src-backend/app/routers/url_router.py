from typing import Annotated

from fastapi import APIRouter, status
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.routers import url_crud
from ..database import get_db
from .url_schemas import UrlResponse, UrlCreate

router = APIRouter(prefix='/urls',
                   tags=['Urls API'])


@router.post("/", response_model=UrlResponse)
def create_url(url: UrlCreate, db: Annotated[Session, Depends(get_db)]):
    return url_crud.create_url(db, url)
