from fastapi import FastAPI
from src.routers import router
from src.auth.router import router as auth_router

app = FastAPI()

app.include_router(router)
app.include_router(auth_router)