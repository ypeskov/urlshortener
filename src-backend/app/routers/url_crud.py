from pprint import pprint
from typing import Type

from sqlalchemy.orm import Session

import app.routers.url_schemas as url_schemas
from ..models.url import Url


# def get_test(db: Session, test_id: int):
#     return db.query(Url).filter(Url.id == test_id).first()


def get_url_by_short(db: Session, short_url: str) -> Type[Url] | None:
    return db.query(Url).filter(Url.short_url == short_url).first()


# def get_tests(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(Test).offset(skip).limit(limit).all()


def create_url(db: Session, url: url_schemas.UrlCreate):
    db_url = Url(short_url=url.short_url, full_url=url.full_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url


# def update_test(db: Session, test: Test, db_test: Test):
#     db_test.email = test.email
#     db_test.is_active = test.is_active
#
#     db.commit()
#     db.refresh(db_test)
#     return db_test