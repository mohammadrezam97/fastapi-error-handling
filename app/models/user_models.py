# app/models/user_models.py
from pydantic import BaseModel, Field

class UserBase(BaseModel):
    name: str = Field(..., example="John Doe")

class UserResponse(UserBase):
    id: int = Field(..., example=1)

class UserCreate(UserBase):
    pass
