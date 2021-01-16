from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from be.core.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=False)

    adverts = relationship("Advert", back_populates="owner")
