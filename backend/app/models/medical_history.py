from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime, timezone

class MedicalHistory(Base):
    __tablename__ = "medical_history"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    notes = Column(String, nullable=True)
    document_path = Column(String, nullable=True)
    created_at = Column(DateTime, default = datetime.now(timezone.utc))
    patient = relationship("User", back_populates="medical_history")