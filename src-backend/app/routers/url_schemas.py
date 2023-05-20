from typing import Optional

from pydantic import BaseModel


class UrlBase(BaseModel):
    pass


class UrlCreate(UrlBase):
    full_url: str


class UrlResponse(UrlBase):
    id: int
    short_url_prefix: str = '/urls/r'
    short_url_path: Optional[str]
    full_url: str

    class Config:
        orm_mode = True
