from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from sqlalchemy import select, insert

from src.schemas.tag import TagCreate, TagRead, TagUpdate
from src.models.tables import tag_table

class TagRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
        
    
    async def create(
        self, 
        tag: TagCreate,
        user_id: int
    ):
        stmt = insert(tag_table).values(**tag.model_dump(), user_id=user_id)
        await self.session.execute(stmt)
        await self.session.commit()
        return {"status":"success"}
    
    
    async def get_all(self, user_id: int) -> List[Optional[TagRead]]:
        query = select(tag_table).where(user_id=user_id)
        result = await self.session.execute(query)
        return result.all()
    
    
    async def delete(self, tag_id: int, user_id: int):
        pass
    
    
    async def update(self, tag: TagUpdate, user_id: int):
        pass