from sqlalchemy.orm import Session
from app.models.medical_history import MedicalHistory
from app.schemas.medical_history import MedicalHistoryCreate

# Create
def create_medical_history(db: Session, history_in: MedicalHistoryCreate, file_path: str = None):
    history = MedicalHistory(
        patient_id = history_in.patient_id,
        notes = history_in.notes,
        document_path = file_path,
    )

    db.add(history)
    db.commit()
    db.refresh(history)
    return history

# Read
def get_all(db: Session):
    return db.query(MedicalHistory).all()
def get_by_patient(db: Session, patient_id: int):
    return db.query(MedicalHistory).filter(MedicalHistory.patient_id == patient_id).all()
def get_by_id(db: Session, medical_history_id: int):
    return db.query(MedicalHistory).filter(MedicalHistory.id == medical_history_id).first()

# Update
def update_medical_history(db: Session, medical_history_id: int, updates: dict):
    db_medical_history = db.query(MedicalHistory).filter(MedicalHistory.id == medical_history_id).first()
    if not db_medical_history:
        return None
    for key, value in updates.items():
        if hasattr(db_medical_history, key) and value is not None:
            setattr(db_medical_history, key, value)
    db.commit()
    db.refresh(db_medical_history)
    return db_medical_history

# Delete
def delete_medical_history(db: Session, medical_history: MedicalHistory):
    db.delete(medical_history)
    db.commit()