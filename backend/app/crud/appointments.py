from sqlalchemy.orm import Session
from app.models.appointment import Appointment
from app.schemas.appointment import AppointmentCreate

# Create
def create_appointment(db:Session, appointment: AppointmentCreate) -> Appointment:
    db_appointment = Appointment(
        patient_id = appointment.patient_id,
        doctor_id = appointment.doctor_id,
        time = appointment.time,
        status = appointment.status,
        notes = appointment.notes,
    )
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

# Read
def get_appointments(db: Session):
    return db.query(Appointment).all()
def get_appointment_by_id(db: Session, appointment_id: int):
    return db.query(Appointment).filter(Appointment.id == appointment_id).first()
def get_appointments_by_doctor(db: Session, doctor_id: int):
    return db.query(Appointment).filter(Appointment.doctor_id == doctor_id).all()
def get_appointments_by_patient(db: Session, patient_id: int):
    return db.query(Appointment).filter(Appointment.patient_id == patient_id).all()

# Update
def update_appointment(db: Session, appointment_id: int, updates: dict):
    db_appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if not db_appointment:
        return None
    for key, value in updates.items():
        setattr(db_appointment, key, value)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

# Delete
def delete_appointment(db: Session, appointment: Appointment):
    db.delete(appointment)
    db.commit()
    