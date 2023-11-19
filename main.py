from fastapi import FastAPI

from users_router import router as user_router
from database import Base, engine


app = FastAPI()

app.include_router(user_router, prefix="/v1")

Base.metadata.create_all(bind=engine)