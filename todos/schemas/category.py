from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str


class categoryRead(CategoryBase):
    id: int
    
    class Config:
        orm_mode: True


class categoryUpdate(CategoryBase):
    category_id: int