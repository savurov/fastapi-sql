from fastapi import FastAPI

from routers.users_router import router as user_router
from routers.messages_router import router as message_router
from routers.auth_router import router as auth_router
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/v1")
app.include_router(message_router, prefix="/v1")
app.include_router(auth_router, prefix="/v1/auth")

# from database import Base, engine
# Base.metadata.create_all(bind=engine)