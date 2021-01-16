from sqlalchemy.orm import Session

from be.core.models.adverts import Advert as AdvertModel
import be.core.schemas.adverts as schemas


def get_advert(db: Session, advert_id: int):
    return db.query(AdvertModel).filter(AdvertModel.id == advert_id).first()


def get_adverts(db: Session, skip: int = 0, limit: int = 50):
    return db.query(AdvertModel).offset(skip).limit(limit).all()


def create_advert(db: Session, advert: schemas.AdvertCreate, owner_id: int):
    db_advert = AdvertModel(**advert.dict(), owner_id=owner_id)
    db.add(db_advert)
    db.commit()
    db.refresh(db_advert)
    return db_advert
