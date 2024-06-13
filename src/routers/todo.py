from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional

from src.auth.auth import current_user
from src.auth.models import User
from src.database import get_async_session
from src.DAL.service.todo_service import TodoService
from src.schemas.todo import TodoCreate, TodoRead, TodoUpdate
from src.utils.responses import get_open_api_unauthorized_access_response
from src.utils.todo_responses import bad_request, forbidden, not_found

router = APIRouter(
    prefix='/todo',
    tags=['Todo']
)

@router.get(
    "/",
    response_model=list[TodoRead],
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_401_UNAUTHORIZED: get_open_api_unauthorized_access_response()}
)
async def get_all(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    service = TodoService(session)
    return await service.get_all(user.id)



@router.post(
    '/',
    response_model=TodoRead,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_401_UNAUTHORIZED: get_open_api_unauthorized_access_response(),
        status.HTTP_400_BAD_REQUEST: bad_request()
    }
)
async def create_todo(
    todo: TodoCreate,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    service = TodoService(session)
    return await service.create(todo, user.id)



@router.patch(
    '/',
    response_model=TodoRead,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_401_UNAUTHORIZED: get_open_api_unauthorized_access_response(),
        status.HTTP_400_BAD_REQUEST: bad_request(),
        status.HTTP_403_FORBIDDEN: forbidden(),
        status.HTTP_404_NOT_FOUND: not_found()
    }
)
async def update_todo(
    todo: TodoUpdate,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    service = TodoService(session)
    return await service.update(todo)



@router.delete(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_401_UNAUTHORIZED: get_open_api_unauthorized_access_response(),
        status.HTTP_403_FORBIDDEN: forbidden(),
        status.HTTP_404_NOT_FOUND: not_found()
    }
)
async def delete_todo(
    todo: TodoRead,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    service = TodoService(session)
    return await service.delete(todo, user.id)