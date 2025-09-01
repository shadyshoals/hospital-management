from sqlalchemy.orm import Session
from app.models.patient import Patient
from app.schemas.patient import PatientCreate

def create_patient(db:Session, patient: PatientCreate):
    db_patient = Patient(**patient.model_dump())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_patients(db: Session):
    return db.query(Patient).all()