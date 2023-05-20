from pprint import pprint

from sqlalchemy.orm import Session

import app.routers.test_schemas as test_schemas
from ..models.test import Test


def get_test(db: Session, test_id: int):
    return db.query(Test).filter(Test.id == test_id).first()


def get_test_by_email(db: Session, email: str):
    return db.query(Test).filter(Test.email == email).first()


def get_tests(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Test).offset(skip).limit(limit).all()


def create_test(db: Session, test: test_schemas.TestCreate):
    fake_hashed_password = test.password + "notreallyhashed"
    db_test = Test(email=test.email, hashed_password=fake_hashed_password)
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test


def update_test(db: Session, test: Test, db_test: Test):
    db_test.email = test.email
    db_test.is_active = test.is_active

    db.commit()
    db.refresh(db_test)
    return db_test