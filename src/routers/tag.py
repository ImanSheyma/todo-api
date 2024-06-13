from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional

from src.auth.auth import current_user
from src.auth.models import User
from src.database import get_async_session
from src.DAL.service.tag_service import CategoryService
from src.schemas.tag import TagCreate, TagRead, TagUpdate
from src.utils.responses import get_open_api_unauthorized_access_response
from src.utils.tag_responses import bad_request, forbidden, not_found

router = APIRouter(
    prefix='/tag',
    tags=['Tag']
)

@router.get(
    "/",
    response_model=List[TagRead],
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_401_UNAUTHORIZED: get_open_api_unauthorized_access_response()}
)
async def get_tags(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
) -> List[Optional[TagRead]]:
    service = CategoryService(session)
    return await service.get_all(user.id)


@router.post(
    '/',
    response_model=TagRead,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_401_UNAUTHORIZED: get_open_api_unauthorized_access_response(),
        status.HTTP_400_BAD_REQUEST: bad_request()
    }
)
async def create_tag(
    tag: TagCreate,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    service = CategoryService(session)
    return await service.create(tag, user.id)


@router.delete(
    '/{tag_id}',
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_401_UNAUTHORIZED: get_open_api_unauthorized_access_response(),
        status.HTTP_403_FORBIDDEN: forbidden(),
        status.HTTP_404_NOT_FOUND: not_found()
    }
)
async def delete_tag(
    tag_id: int,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    service = CategoryService(session)
    return await service.delete(tag_id, user.id)


@router.patch(
    "/",
    response_model=TagRead,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_401_UNAUTHORIZED: get_open_api_unauthorized_access_response(),
        status.HTTP_403_FORBIDDEN: forbidden(),
        status.HTTP_404_NOT_FOUND: not_found()
    }
)
async def update(
    tag: TagUpdate,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    service = CategoryService(session)
    return await service.update(tag, user.id)