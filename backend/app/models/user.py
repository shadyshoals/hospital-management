# backend/app/models/__init__.py
# This can be empty, or you can import models here

# Optional: Expose models when importing the package
#from .patient import Patient  # Example

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False) # e.g. admin, doctor, nurse

    created_at = Column(DateTime, default=datetime.now(timezone.utc))
