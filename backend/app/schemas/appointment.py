from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional
from app.schemas.user import UserRead

class UserInfo(BaseModel):
    id: int
    first_name: str
    last_name: str

    class Config:
        orm_mode = True

class AppointmentStatus(str, Enum):
    scheduled = "scheduled"
    completed = "completed"
    canceled = "canceled"

class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    scheduled_time: datetime
    status: AppointmentStatus = AppointmentStatus.scheduled

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentRead(AppointmentBase):
    id: int
    doctor: Optional[UserRead]
    patient: Optional[UserRead]
    scheduled_time: datetime
    status:AppointmentStatus
    created_at: datetime

    class Config:
        orm_mode = True

