from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from be.core.db import Base


class Advert(Base):
    __tablename__ = "adverts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="adverts")
