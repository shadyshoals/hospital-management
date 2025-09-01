from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.patient import PatientCreate, PatientRead
from app.crud.patient import create_patient, get_patients

router = APIRouter(prefix="/patients", tags=["patients"])

# GET
@router.get("/", response_model=list[PatientRead])
def list_patients(db:Session = Depends(get_db)):
    return get_patients(db)

# POST
@router.post("/", response_model=PatientRead)
def add_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    return create_patient(db, patient)

