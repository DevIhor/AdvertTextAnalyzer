from typing import Optional

from pydantic.main import BaseModel


class AdvertBase(BaseModel):
    title: str
    description: Optional[str] = None


class AdvertCreate(AdvertBase):
    pass


class Advert(AdvertBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
