from typing import Annotated, List

from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.routers import url_crud
from ..database import get_db
from .url_schemas import UrlResponse, UrlCreate

router = APIRouter(prefix='/urls')


@router.post("/", response_model=UrlResponse)
def create_test(url: UrlCreate, db: Annotated[Session, Depends(get_db)]):
    db_url = url_crud.get_url_by_short(db, short_url=url.short_url)
    if db_url:
        raise HTTPException(status_code=400, detail="Short URL already exists")
    return url_crud.create_url(db, url)


# @router.put('/', response_model=Url)
# def update_test(db: Annotated[Session, Depends(get_db)], test: Url):
#     db_test = test_crud.get_test(db, test.id)
#     if not db_test:
#         raise HTTPException(status_code=404, detail='Test not found')
#     db_test = test_crud.update_test(db, test, db_test)
#     return db_test
#
# @router.get("/", response_model=List[Url])
# def read_tests(db: Annotated[Session, Depends(get_db)],
#                skip: int = 0,
#                limit: int = 100, ):
#     users = test_crud.get_tests(db, skip=skip, limit=limit)
#     return users


# @router.get("/{test_id}", response_model=Url)
# def read_test(test_id: int, db: Annotated[Session, Depends(get_db)]):
#     db_test = test_crud.get_test(db, test_id=test_id)
#     if db_test is None:
#         raise HTTPException(status_code=404, detail="Test not found")
#     return db_test
