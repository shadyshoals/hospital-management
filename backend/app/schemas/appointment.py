from pydantic import BaseModel
from datetime import datetime
from enum import Enum

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
    created_at: datetime

    class Config:
        orm_mode = True

