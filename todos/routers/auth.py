from fastapi import APIRouter

from ..auth.auth import auth_backend
from ..schemas.user import UserRead, UserCreate
from ..auth.users import fastapi_users

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
)