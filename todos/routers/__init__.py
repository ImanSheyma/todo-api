from fastapi import APIRouter

from .todos import router as todos_router
from .categories import router as categories_router
from .users import router as users_router
from .auth import router as auth_router

router = APIRouter(
    prefix='/api'
)

router.include_router(todos_router)
router.include_router(categories_router)
router.include_router(users_router)
router.include_router(auth_router)