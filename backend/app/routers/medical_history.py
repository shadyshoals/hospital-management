from dotenv import load_dotenv
from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException, status
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import os, shutil
from app.database import get_db
from app.models.medical_history import MedicalHistory
from app.schemas.medical_history import MedicalHistoryOut, MedicalHistoryCreate, MedicalHistoryUpdate
from app.utils.file_services import save_uploaded_file
import app.crud.medical_history as medical_history_crud
from app.utils.security import get_current_user
from app.models.user import User

router = APIRouter(prefix="/medical_history", tags=["Medical History"])


@router.post("/", response_model=MedicalHistoryOut)
def create_medical_history(
    patient_id: int = Form(...),
    notes: str = Form(None),
    file: UploadFile = File(None),
    db: Session = Depends(get_db),
):
    file_path = None
    if file:
        file_path = save_uploaded_file(patient_id, file)

    history_in = MedicalHistoryCreate(patient_id=patient_id, notes=notes)
    return medical_history_crud.create_medical_history(db, history_in, file_path)

@router.get("/", response_model=list[MedicalHistoryOut])
def get_all_medical_histories(db: Session = Depends(get_db)):
    return medical_history_crud.get_all(db)

@router.get("/by-patient/{patient-id}", response_model=list[MedicalHistoryOut])
def get_by_patient_id(patient_id: int, db: Session = Depends(get_db)):
    return medical_history_crud.get_by_patient(db, patient_id)

@router.get("/{medical-history-id}", response_model=MedicalHistoryOut)
def get_by_id(medical_history_id: int, db: Session = Depends(get_db)):
    return medical_history_crud.get_by_id(db, medical_history_id)

#todo: Move this db operation into crud layer -- actually move all of them
@router.get("/medical-history/{medical-history-id}/download")
def download_medical_history(
    medical_history_id: int,
    # current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # medical_history_record = db.query(MedicalHistory).filter(MedicalHistory.id == medical_history_id).first()
    medical_history_record = medical_history_crud.get_by_id(db, medical_history_id)

    if not medical_history_record:
        raise HTTPException(status=status.HTTP_404_NOT_FOUND, detail="File not found")
    return FileResponse(path=medical_history_record.document_path)

@router.patch("/{medical-history-id}", response_model=MedicalHistoryUpdate)
def update_medical_history(
    medical_history_id: int, 
    medical_history_update: MedicalHistoryUpdate, 
    db: Session = Depends(get_db)
):
    updates = medical_history_update.dict(exclude_unset=True)
    medical_history = medical_history_crud.update_medical_history(db, medical_history_id, updates)
    if not medical_history:
        raise HTTPException(status_code=404, detail="Medical history not found")
    return medical_history

@router.delete("/{medical-history-id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medical_history(
    medical_history_id: int,
    db: Session = Depends(get_db)
):
    db_medical_history = medical_history_crud.get_by_id(db, medical_history_id)

    if not db_medical_history:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Medical history not found")
    
    medical_history_crud.delete_medical_history(db, db_medical_history)
    return None