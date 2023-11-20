from fastapi import FastAPI

from routers.users_router import router as user_router
from routers.messages_router import router as message_router



app = FastAPI()

app.include_router(user_router, prefix="/v1")
app.include_router(message_router, prefix="/v1")

# from database import Base, engine
# Base.metadata.create_all(bind=engine)