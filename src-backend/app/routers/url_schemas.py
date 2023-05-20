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
    success: bool = True

    class Config:
        orm_mode = True

class ErrorGenerateShortUrl(BaseModel):
    success: bool = False
    msg: str = 'Error while generation short URL'
    code: int = 450
