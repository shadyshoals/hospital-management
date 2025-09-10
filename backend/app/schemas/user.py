from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional
from app.models import UserRole

class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str
    # role: UserRole

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    # role: UserRole | None = None

class UserRead(UserBase):
    id: int
    role: str
    created_at: datetime
    
    class Config:
        orm_mode = True

class AdminCreate(UserBase):
    department: Optional[str]
    permission_level: int

class AdminOut(UserBase):
    id: int
    role: str = UserRole.admin
    department: Optional[str]
    permission_level: int
    created_at: datetime
    
    class Config:
        orm_mode = True

class DoctorCreate(UserBase):
    specialty: Optional[str]
    doctor_license_number: Optional[str]

class DoctorOut(UserBase):
    id: int
    role: str = UserRole.doctor
    specialty: Optional[str]
    doctor_license_number: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True

class NurseCreate(UserBase):
    unit: Optional[str]
    shift: Optional[str]

class NurseOut(UserBase):
    id: int
    role: str = UserRole.nurse
    unit: Optional[str]
    shift: Optional[str]
    created_at: datetime

    class Config: 
        orm_mode = True

class PharmacistCreate(UserBase):
    pharmacist_license_number: Optional[str]
    pharmacy_location: Optional[str]

class PharmacistOut(UserBase):
    id: int
    role: str = UserRole.pharmacist
    pharmacist_license_number: Optional[str]
    pharmacy_location: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True

class PhysiotherapistCreate(UserBase):
    specialization: Optional[str]
    physiotherapist_license_number: Optional[str]

class PhysiotherapistOut(UserBase):
    id: int
    role: str = UserRole.physiotherapist
    specialization: Optional[str]
    physiotherapist_license_number: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True

class RecreationCreate(UserBase):
    office_location: Optional[str]
    programs_responsible_for: Optional[str]

class RecreationOut(UserBase):
    id: int
    role: str = UserRole.recreation
    office_location: Optional[str]
    programs_responsible_for: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True

class PatientCreate(UserBase):
    medical_record_number: str
    medical_history: Optional[str]
    emergency_contact: Optional[str]

class PatientOut(UserBase):
    id: int
    role: str = UserRole.patient
    medical_record_number: str
    medical_history: Optional[str]
    emergency_contact: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
