from sqlalchemy.orm import Session
from app import models
from app.schemas import user as user_schema
from passlib.context import CryptContext
from app.models import user as user_models
from app.models.user import Admin, Doctor, Nurse, Pharmacist, Physiotherapist, Recreation, Patient, UserRole

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Create
def create_admin(db: Session, admin_data: dict) -> Admin:
    """
    Create an admin user.
    'admin_data' should already contain hashed_password and all fields from AdminCreate
    """
    db_admin = Admin(**admin_data)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin
def create_doctor(db: Session, doctor_data: dict) -> Doctor:
    db_doctor = Doctor(**doctor_data)
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor
def create_nurse(db: Session, nurse_data: dict) -> Nurse:
    db_nurse = Nurse(**nurse_data)
    db.add(db_nurse)
    db.commit()
    db.refresh(db_nurse)
    return db_nurse
def create_pharmacist(db: Session, pharmacist_data: dict) -> Pharmacist:
    db_pharmacist = Pharmacist(**pharmacist_data)
    db.add(db_pharmacist)
    db.commit()
    db.refresh(db_pharmacist)
    return db_pharmacist
def create_physiotherapist(db: Session, physiotherapist_data: dict) -> Physiotherapist:
    db_physiotherapist = Physiotherapist(**physiotherapist_data)
    db.add(db_physiotherapist)
    db.commit()
    db.refresh(db_physiotherapist)
    return db_physiotherapist
def create_recreation(db: Session, recreation_data: dict) -> Recreation:
    db_recreation = Recreation(**recreation_data)
    db.add(db_recreation)
    db.commit()
    db.refresh(db_recreation)
    return db_recreation
def create_patient(db: Session, patient_data: dict) -> Patient:
    db_patient = Patient(**patient_data)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def create_user(db:Session, user: user_schema.UserCreate):
    hashed_pw = pwd_context.hash(user.password)
    db_user = models.user.User(
        username=user.username,
        hashed_password=hashed_pw,
        first_name=user.first_name,
        last_name=user.last_name,
        role=user.role,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# READ
def get_user(db:Session, user_id: int):
    return db.query(models.user.User).filter(models.user.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.user.User).offset(skip).limit(limit).all()

def get_by_role(db: Session, role: UserRole):
    return db.query(models.user.User).filter(models.User.type == role.value).all()

def get_by_first_name(db: Session, first_name: str):
    return db.query(models.user.User).filter(models.User.first_name == first_name).all()

# UPDATE
def update_user(db: Session, user_id: int, updates: dict):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        return None
    for key, value in updates.items():
        if hasattr(db_user, key) and value is not None:
            setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

# DELETE
def delete_user(db:Session, user: models.User):
    db.delete(user)
    db.commit()