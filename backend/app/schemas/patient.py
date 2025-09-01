from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timezone

class PatientBase(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: Optional[datetime] = None
    is_discharged: Optional[bool] = False
    assigned_doctor_id: Optional[int] = None

class PatientCreate(PatientBase):
    pass

class PatientRead(PatientBase):
    id: int

    class Config:
        orm_mode = True
        