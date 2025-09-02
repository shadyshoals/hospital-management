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

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    role = Column(SQLEnum(UserRole), nullable=False, default=UserRole.doctor) # e.g. admin, doctor, nurse

    created_at = Column(DateTime, default=datetime.now(timezone.utc))

# Relationships
appointments = relationship("Appointment", back_populates="doctor")