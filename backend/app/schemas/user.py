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
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    # role: UserRole | None = None

class UserRead(UserBase):
    id: int
    #role: str
    created_at: datetime
    
    class Config:
        orm_mode = True

class AdminCreate(UserCreate):
    department: Optional[str]
    permission_level: Optional[int]

class AdminOut(UserBase):
    id: int
    role: str = UserRole.admin
    department: Optional[str]
    permission_level: int
    created_at: datetime
    
    class Config:
        orm_mode = True

class AdminUpdate(BaseModel):
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    department: Optional[str] = None
    permission_level: Optional[int] = None

class DoctorCreate(UserCreate):
    specialty: Optional[str]
    doctor_license_number: Optional[str]

class DoctorOut(UserBase):
    id: int
    role: str = UserRole.doctor
    specialty: Optional[str] = None
    doctor_license_number: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True

class DoctorUpdate(BaseModel):
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    specialty: Optional[str] = None
    doctor_license_number: Optional[str]

class NurseCreate(UserCreate):
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

class NurseUpdate(BaseModel):
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    unit: Optional[str]
    shift: Optional[str]

class PharmacistCreate(UserCreate):
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

class PharmacistUpdate(BaseModel):
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    pharmacist_license_number: Optional[str] = None
    pharmacy_location: Optional[str] = None

class PhysiotherapistCreate(UserCreate):
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

class PhysiotherapistUpdate(BaseModel):
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    specialization: Optional[str] = None
    physiotherapist_license_number: Optional[str] = None

class RecreationCreate(UserCreate):
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

class RecreationUpdate(BaseModel):
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    office_location: Optional[str] = None
    programs_responsible_for: Optional[str] = None

class PatientCreate(UserCreate):
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

class PatientUpdate(BaseModel):
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    medical_record_number: Optional[str] = None
    medical_history: Optional[str] = None
    emergency_contact: Optional[str] = None