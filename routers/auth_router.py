from fastapi import APIRouter, HTTPException, status, Depends, Response
from database import get_db
from sqlalchemy.orm import Session
import models, jwt

router = APIRouter()

from pydantic import BaseModel, EmailStr, Field

class LoginForm(BaseModel):
    email: EmailStr = Field(..., examples=["user@example.com"])
    password: str = Field(..., min_length=1, examples=["yourpassword"])


@router.post("/login")
def login(response: Response, login_form: LoginForm, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == login_form.email).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверные учетные данные",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = jwt.create_access_token(data={"sub": user.email})
    #access_token = "hello It's access"
    response.set_cookie(key="access_token", value=access_token, httponly=True)
    return {"message": "Успешный вход"}
