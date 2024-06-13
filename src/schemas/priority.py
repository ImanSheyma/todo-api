from pydantic import BaseModel

class Priority(BaseModel):
    id: int
    name: str