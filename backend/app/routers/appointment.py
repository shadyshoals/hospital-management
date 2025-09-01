from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.appointment import AppointmentCreate, AppointmentRead
from app.crud.appointments import create_appointment, get_appointments

router = APIRouter(prefix="/appointments", tags=["appointments"])

# GET
@router.get("/", response_model=list[AppointmentRead])
def list_appointments(db:Session = Depends(get_db)):
    return get_appointments(db)

# POST
@router.post("/", response_model=AppointmentRead)
def add_appointments(appointments: AppointmentCreate, db: Session = Depends(get_db)):
    return create_appointment(db, appointments)

