from pprint import pprint
from typing import Annotated, List

from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.routers import test_crud
from ..database import get_db
from .test_schemas import Test, TestCreate

router = APIRouter(prefix='/tests')


@router.post("/", response_model=Test)
def create_test(test: TestCreate, db: Annotated[Session, Depends(get_db)]):
    db_test = test_crud.get_test_by_email(db, email=test.email)
    if db_test:
        raise HTTPException(status_code=400, detail="Email already registered")
    return test_crud.create_test(db=db, test=test)


@router.put('/', response_model=Test)
def update_test(db: Annotated[Session, Depends(get_db)], test: Test):
    db_test = test_crud.get_test(db, test.id)
    if not db_test:
        raise HTTPException(status_code=404, detail='Test not found')
    db_test = test_crud.update_test(db, test, db_test)
    return db_test

@router.get("/", response_model=List[Test])
def read_tests(db: Annotated[Session, Depends(get_db)],
               skip: int = 0,
               limit: int = 100, ):
    users = test_crud.get_tests(db, skip=skip, limit=limit)
    return users


@router.get("/{test_id}", response_model=Test)
def read_test(test_id: int, db: Annotated[Session, Depends(get_db)]):
    db_test = test_crud.get_test(db, test_id=test_id)
    if db_test is None:
        raise HTTPException(status_code=404, detail="Test not found")
    return db_test
