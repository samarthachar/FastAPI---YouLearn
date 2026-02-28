from pydantic import BaseModel, EmailStr, Field # type: ignore

class UserCreate(BaseModel):
    email: EmailStr
    full_name: str = Field(min_length=2, max_length=100)
    password: str = Field(min_length=8, max_length=128)

class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    
    class Config:
        from_attributes = True