from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field # type: ignore 

class TestCreate(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=1000)
    is_published: bool = False
    owner_id: int


class TestOut(BaseModel):
    id: int
    title: str
    description: str
    is_published: bool

    owner_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True