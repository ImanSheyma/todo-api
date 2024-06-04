from fastapi import FastAPI
from todos.routers import router

app = FastAPI()

app.include_router(router)