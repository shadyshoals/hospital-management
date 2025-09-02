from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    # Software operators, directors...
    admin = "admin"
    # Medical Personnel
    doctor = "doctor"
    nurse = "nurse"
    psw = "psw"
    nurse_manager = "nurse manager"
    pharmacist = "pharmacist"
    physiotherapist = "physiotherapist"
    # Social Work
    recreation = "recreation"
    recreation_manager = "recreation manager"
    social_worker = "social worker"
    counsellor = "counsellor"

class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str
    role: UserRole

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    role: UserRole | None = None

class UserRead(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True
        