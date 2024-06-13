from fastapi import APIRouter

from src.routers.todo import router as todo_router
from src.routers.tag import router as tag_router

router = APIRouter(
    prefix='/api'
)

router.include_router(todo_router)
router.include_router(tag_router)