from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from database import get_db
import schemas, models


router = APIRouter()


@router.get("/messages/", response_model=list[schemas.Message])
def read_messages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    messages = db.query(models.Message).offset(skip).limit(limit).all()
    return messages


@router.post("/messages/", response_model=schemas.Message)
def create_message(message: schemas.MessageCreate, db: Session = Depends(get_db)):
    db_message = models.Message(body=message.body, author=message.author)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message
