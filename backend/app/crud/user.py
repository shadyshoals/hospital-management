from sqlalchemy.orm import Session
from app import models
from app.schemas import user as user_schema
from passlib.context import CryptContext
from app.models.user import User, Admin, Doctor, Nurse, Pharmacist, Physiotherapist, Recreation, Patient, UserRole

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Create
def create_admin(db: Session, admin: user_schema.AdminCreate) -> Admin:
    """
    Create an admin user.
    'admin_data' should already contain hashed_password and all fields from AdminCreate
    """
    hashed_pw = pwd_context.hash(admin.password)
    db_admin = Admin(
        username = admin.username,
        hashed_password = hashed_pw,
        first_name = admin.first_name,
        last_name = admin.last_name,
        department = admin.department,
        permission_level = admin.permission_level, 
    )
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin
def create_doctor(db: Session, doctor: user_schema.DoctorCreate) -> Doctor:
    hashed_pw = pwd_context.hash(doctor.password)
    db_doctor = Doctor(
        username = doctor.username,
        hashed_password = hashed_pw,
        first_name = doctor.first_name,
        last_name = doctor.last_name,
        specialty = doctor.specialty,
        doctor_license_number = doctor.doctor_license_number
    )
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor
def create_nurse(db: Session, nurse: user_schema.NurseCreate) -> Nurse:
    hashed_pw = pwd_context.hash(nurse.password)
    db_nurse = Doctor(
        username = nurse.username,
        hashed_password = hashed_pw,
        first_name = nurse.first_name,
        last_name = nurse.last_name,
        unit = nurse.unit,
        shift = nurse.shift,
    )
    db.add(db_nurse)
    db.commit()
    db.refresh(db_nurse)
    return db_nurse
def create_pharmacist(db: Session, pharmacist: user_schema.PharmacistCreate) -> Pharmacist:
    hashed_pw = pwd_context.hash(pharmacist.password)
    db_pharmacist = Pharmacist(
        username = pharmacist.username,
        hashed_password = hashed_pw,
        first_name = pharmacist.first_name,
        last_name = pharmacist.last_name,
        pharmacist_license_number = pharmacist.pharmacist_license_number,
        pharmacy_location = pharmacist.pharmacy_location,
    )
    db.add(db_pharmacist)
    db.commit()
    db.refresh(db_pharmacist)
    return db_pharmacist
def create_physiotherapist(db: Session, physiotherapist: user_schema.PhysiotherapistCreate) -> Physiotherapist:
    hashed_pw = pwd_context.hash(physiotherapist.password)
    db_physiotherapist = Physiotherapist(
        username = physiotherapist.username,
        hashed_password = hashed_pw,
        first_name = physiotherapist.first_name,
        last_name = physiotherapist.last_name,
        specialization = physiotherapist.specialization,
        physiotherapist_license_number = physiotherapist.physiotherapist_license_number,
    )
    db.add(db_physiotherapist)
    db.commit()
    db.refresh(db_physiotherapist)
    return db_physiotherapist
def create_recreation(db: Session, recreation: user_schema.RecreationCreate) -> Recreation:
    hashed_pw = pwd_context.hash(recreation.password)
    db_recreation = Recreation(
        username = recreation.username,
        hashed_password = hashed_pw,
        first_name = recreation.first_name,
        last_name = recreation.last_name,
        office_location = recreation.office_location,
        programs_responsible_for = recreation.programs_responsible_for,
    )
    db.add(db_recreation)
    db.commit()
    db.refresh(db_recreation)
    return db_recreation
def create_patient(db: Session, patient: user_schema.PatientCreate) -> Patient:
    hashed_pw = pwd_context.hash(patient.password)
    db_patient = Patient(
        username = patient.username,
        hashed_password = hashed_pw,
        first_name = patient.first_name,
        last_name = patient.last_name,
        medical_record_number = patient.medical_record_number,
        medical_history = patient.medical_history,
        emergency_contact = patient.emergency_contact,
    )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

# def create_user(db:Session, user: user_schema.UserCreate):
#     hashed_pw = pwd_context.hash(user.password)
#     db_user = models.user.User(
#         username=user.username,
#         hashed_password=hashed_pw,
#         first_name=user.first_name,
#         last_name=user.last_name,
#         role=user.role,
#     )
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# READ
def get_user(db:Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def get_by_role(db: Session, role: UserRole):
    return db.query(User).filter(User.type == role.value).all()

def get_by_first_name(db: Session, first_name: str):
    return db.query(User).filter(User.first_name == first_name).all()

# UPDATE
def update_user(db: Session, user_id: int, updates: dict):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    for key, value in updates.items():
        if hasattr(db_user, key) and value is not None:
            setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

# DELETE
def delete_user(db:Session, user: User):
    db.delete(user)
    db.commit()