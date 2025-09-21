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
    missed = "missed"

class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    time: datetime
    status: AppointmentStatus = AppointmentStatus.scheduled
    notes: Optional[str] = None

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentUpdate(BaseModel):
    patient_id: int
    doctor_id: int
    time: Optional[datetime] = None
    status: Optional [AppointmentStatus] = None
    notes: Optional[str] = None

class AppointmentOut(AppointmentBase):
    id: int
    doctor: UserRead
    patient: UserRead
    time: datetime
    status:AppointmentStatus
    created_at: datetime

    class Config:
        orm_mode = True
