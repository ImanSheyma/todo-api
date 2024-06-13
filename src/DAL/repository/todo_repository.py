from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from sqlalchemy import select, insert, update

from src.schemas.todo import TodoCreate, TodoRead, TodoUpdate
from src.models.tables import todo_table

class TodoRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
        
    
    async def create(
        self, 
        todo: TodoCreate,
        user_id: int
    ):
        stmt = insert(todo_table).values(**todo.model_dump(), user_id=user_id)
        await self.session.execute(stmt)
        await self.session.commit()
        return {"status":"success"}
    
    
    async def get_all(self, user_id):
        query = select(todo_table)
        result = await self.session.execute(query)
        return result.all()
    
    
    async def update(self, todo: TodoUpdate) -> TodoRead:
        stmt = update(todo_table).values(**todo.model_dump())
        await self.session.execute(stmt)
        await self.session.commit()
        return {"status":"success"}
    
    async def delete(self, todo: TodoRead, user_id: int):
        pass