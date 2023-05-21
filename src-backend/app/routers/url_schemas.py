from typing import Optional

from pydantic import BaseModel


class UrlBase(BaseModel):
    pass


class UrlCreate(UrlBase):
    full_url: str


class UrlResponse(UrlBase):
    id: int
    short_url_prefix: str
    short_url_path: Optional[str]
    full_url: str
    short_url: str
    success: bool = True

    class Config:
        orm_mode = True
