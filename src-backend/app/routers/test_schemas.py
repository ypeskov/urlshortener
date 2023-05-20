from pydantic import BaseModel


class TestBase(BaseModel):
    email: str


class TestCreate(TestBase):
    password: str


class Test(TestBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
