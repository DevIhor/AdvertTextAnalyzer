from typing import List

from pydantic.main import BaseModel

from be.core.schemas.adverts import Advert


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    is_staff: bool
    adverts: List[Advert] = []

    class Config:
        orm_mode = True
