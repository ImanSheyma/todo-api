from pydantic import BaseModel

from .priority import Priority
from category import CategoryBase

class TodoBase(BaseModel):
    content: str

class TodoRead(TodoBase):
    id: int
    is_completed: bool
    priority: Priority
    category: CategoryBase
    
    class Congig:
        orm_mode: True


class TodoCreate(TodoBase):
    priority_id: int
    category_id: int


class TodoUpdate(TodoCreate):
    is_completede: bool