from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional

from src.DAL.repository.todo_repository import TodoRepository
from src.schemas.todo import TodoCreate, TodoRead, TodoUpdate


class TodoService:
    def __init__(self, session: AsyncSession):
        self.repository = TodoRepository(session)
        
    
    async def create(
        self, 
        todo: TodoCreate,
        user_id: int
    ):
        return await self.repository.create(todo, user_id)
    
    
    async def get_all(self, user_id: int):
        return await self.repository.get_all(user_id)
    
    
    async def update(self, todo: TodoUpdate):
        return await self.repository.update(todo)
    
    async def delete(self, todo: TodoRead, user_id: int):
        return await self.repository.delete(todo, user_id)