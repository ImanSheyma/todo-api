from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..auth.users import current_user
from ..auth.database import User, get_async_session

router = APIRouter(
    prefix='/todos',
    tags=['Todos']
)

@router.get("/")
def get_todo(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    return f"Hello, {user.email}"


@router.post('/')
async def create_todo(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    return 'created todo'


@router.put('/')
async def update_todo(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    return 'updated_todo'


@router.delete('/')
async def delete_todo(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    return 'deleted todo'