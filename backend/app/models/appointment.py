from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base
from enum import Enum

class AppointmentStatus(str, Enum):
    scheduled = "scheduled"
    completed = "complete"
    canceled = "canceled"
    missed = "missed"

class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    patient_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    doctor = relationship("User", foreign_keys=[doctor_id], back_populates="appointments_as_doctor")
    patient = relationship("User", foreign_keys=[patient_id], back_populates="appointments_as_patient")
    time = Column(DateTime, nullable=False)
    status = Column(SQLEnum(AppointmentStatus, name="appointmentstatus"), default=AppointmentStatus.scheduled, nullable=False)
    notes = Column(String, nullable=True)

    created_at = Column(DateTime, default = datetime.now(timezone.utc))
