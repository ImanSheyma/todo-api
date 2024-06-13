from pydantic import BaseModel


class TagCreate(BaseModel):
    name: str


class TagRead(TagCreate):
    id: int
    
    class Config:
        orm_mode: True
        

class TagUpdate(TagRead):
    pass