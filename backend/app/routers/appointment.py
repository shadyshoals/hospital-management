from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.appointment import AppointmentCreate, AppointmentOut
# from app.crud.appointments import create_appointment, get_appointments
import app.crud.appointments as appointments_crud
from app.models.user import Admin, Doctor
from app.utils.roles import require_role

router = APIRouter(prefix="/appointments", tags=["appointments"])

# GET
@router.get("/", response_model=list[AppointmentOut])
def get_appointments(db:Session = Depends(get_db)):
    return appointments_crud.get_appointments(db)

# POST
@router.post("/", response_model=AppointmentOut)
def create_appointment(
    appointment: AppointmentCreate, 
    db: Session = Depends(get_db),
    _: any = Depends(require_role([Admin, Doctor]))
):
    
    return appointments_crud.create_appointment(db, appointment)

