from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timezone

class UserBase(BaseModel):
    username: str
    hashed_password: str
    first_name: str
    last_name: str
    role: str

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True
        