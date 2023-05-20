import string
from random import choice
from typing import Type

from sqlalchemy.orm import Session

import app.routers.url_schemas as url_schemas
from ..models.url import Url


def get_url_by_short(db: Session, short_url: str) -> Type[Url] | None:
    return db.query(Url).filter(Url.short_url_path == short_url).first()


def generate_short_id(num_of_chars: int):
    """Function to generate short_id of specified number of characters"""
    return ''.join(choice(string.ascii_letters + string.digits) for _ in range(num_of_chars))


def create_url(db: Session, url: url_schemas.UrlCreate):
    random_str = generate_short_id(5)
    db_url = Url(full_url=url.full_url,
                 short_url_prefix='',
                 short_url_path=random_str)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url
