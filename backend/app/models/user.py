# backend/app/models/__init__.py
# This can be empty, or you can import models here

# Optional: Expose models when importing the package
#from .patient import Patient  # Example

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base
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
    # Other
    patient = "patient"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    # role = Column(SQLEnum(UserRole), nullable=False) # e.g. admin, doctor, nurse

    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    type = Column(String(50))  # for inheritance
    __mapper_args__ = {
            "polymorphic_identity": "user",
            "polymorphic_on": type
    }

    # Relationships (shared across subclasses)
    appointments_as_doctor = relationship(
        "Appointment", 
        foreign_keys="Appointment.doctor_id", 
        back_populates="doctor",
        cascade="all, delete-orphan"
    )
    appointments_as_patient = relationship(
        "Appointment", 
        foreign_keys="Appointment.patient_id", 
        back_populates="patient",
        cascade="all, delete-orphan"
    )

    medical_history = relationship(
        "MedicalHistory",
        back_populates="patient",
        cascade="all, delete-orphan"
    )

##### SUBCLASSES ######

class Admin(User):
    department = Column(String, nullable=True)
    permission_level = Column(Integer, nullable=True)
    
    __mapper_args__ = {"polymorphic_identity": UserRole.admin}

class Doctor(User):
    specialty = Column(String, nullable=True)
    doctor_license_number = Column(String, nullable=True)

    __mapper_args__ = {"polymorphic_identity": UserRole.doctor}

class Nurse(User):
    unit = Column(String, nullable=True)
    shift = Column(String, nullable=True)

    __mapper_args__ = {"polymorphic_identity": UserRole.nurse}

class Pharmacist(User):
    pharmacist_license_number = Column(String, nullable=True)
    pharmacy_location = Column(String, nullable=True)

    __mapper_args__ = {"polymorphic_identity": UserRole.pharmacist}

class Physiotherapist(User):
    specialization = Column(String, nullable=True)
    physiotherapist_license_number = Column(String, nullable=True)

    __mapper_args__ = {"polymorphic_identity": UserRole.physiotherapist}

class Recreation(User):
    office_location = Column(String, nullable=True)
    programs_responsible_for = Column(String, nullable=True)

    __mapper_args__ = {"polymorphic_identity": UserRole.recreation}

class Patient(User):
    medical_record_number = Column(String, nullable=True)
    # medical_history = Column(String, nullable=True)
    emergency_contact = Column(String, nullable=True)

    __mapper_args__ = {"polymorphic_identity": UserRole.patient}