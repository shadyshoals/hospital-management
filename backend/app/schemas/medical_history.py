from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timezone

class MedicalHistoryBase(BaseModel):
    notes: Optional[str] = None

class MedicalHistoryCreate(MedicalHistoryBase):
    patient_id: int

class MedicalHistoryOut(MedicalHistoryBase):
    id: int
    patient_id: int
    document_path: Optional[str] = None
    created_at: datetime
    notes: str
    
    class Config:
        orm_mode = True

class MedicalHistoryUpdate(MedicalHistoryBase):
    patient_id: Optional[int] = None
    document_path: Optional[str] = None
    notes: Optional[str] = None