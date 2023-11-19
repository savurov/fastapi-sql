from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from database import get_db
import schemas, repositories


router = APIRouter()


@router.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = repositories.get_users(db, skip=skip, limit=limit)
    return users


@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = repositories.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return repositories.create_new_user(db=db, user=user)
