from pydantic import BaseModel

from src.schemas.priority import Priority
from src.schemas.tag import TagRead

class TodoBase(BaseModel):
    content: str

class TodoRead(TodoBase):
    id: int
    is_completed: bool
    priority: Priority
    tag: TagRead
    
    class Congig:
        orm_mode: True


class TodoCreate(TodoBase):
    priority_id: int
    tag_id: int


class TodoUpdate(TodoCreate):
    is_completede: bool