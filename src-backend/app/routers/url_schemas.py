from pydantic import BaseModel


class UrlBase(BaseModel):
    short_url: str
    full_url: str


class UrlCreate(UrlBase):
    pass


class UrlResponse(UrlBase):
    id: int

    class Config:
        orm_mode = True
