from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from be.core.db import get_db
import be.core.cruds.users as cruds
import be.core.schemas.users as schemas

router = APIRouter(prefix='/users', tags=["users"], dependencies=[Depends(get_db)],
                   responses={404: {"description": "Not Found"}})


@router.get("/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return cruds.get_users(db, skip=skip, limit=limit)


@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = cruds.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
