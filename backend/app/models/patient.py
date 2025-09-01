from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base



class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(DateTime, nullable=True)
    is_discharged = Column(Boolean, default=False)
    assigned_doctor_id = Column(Integer, ForeignKey("users.id"))

    doctor = relationship("User")
    created_at = Column(DateTime, default = datetime.now(timezone.utc))
