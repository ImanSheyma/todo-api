from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional

from src.DAL.repository.tag_repository import TagRepository
from src.schemas.tag import TagRead, TagCreate, TagUpdate


class CategoryService:
    def __init__(self, session: AsyncSession):
        self.repository = TagRepository(session)
        
    
    async def create(
        self, 
        tag: TagCreate,
        user_id: int
    ):
        return await self.repository.create(tag, user_id)
    
    
    async def get_all(self, user_id: int) -> List[Optional[TagRead]]:
        return await self.repository.get_all(user_id)
    
    
    async def delete(self, tag_id: int, user_id: int):
        return await self.repository.delete(tag_id, user_id)
    
    
    async def update(self, tag: TagUpdate, user_id: int):
        return await self.repository.update(tag, user_id)