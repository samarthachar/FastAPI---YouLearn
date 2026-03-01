from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field # type: ignore 

class TestCreate(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=1000)


class TestOut(BaseModel):
    id: int
    title: str
    description: str | None = None
    is_published: bool

    owner_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class TestUpdate(BaseModel):
    title: str | None = None 
    description: str | None = None
    is_published: bool = False