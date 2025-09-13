from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.crud import user as user_crud
from app.schemas import user as user_schema
from app.database import get_db
from app.schemas.user import AdminCreate, AdminOut, DoctorCreate, DoctorOut, NurseCreate, NurseOut, PharmacistCreate, PharmacistOut, PhysiotherapistCreate, PhysiotherapistOut, RecreationCreate, RecreationOut, PatientCreate, PatientOut, UserRole
# from app.dependencies import pwd_context
from typing import Union

UserOut = Union[
    user_schema.AdminOut,
    user_schema.DoctorOut,
    user_schema.NurseOut,
    user_schema.PharmacistOut,
    user_schema.PhysiotherapistOut,
    user_schema.RecreationOut,
    user_schema.PatientOut,
]



router = APIRouter(prefix="/users", tags=["users"])

########################################################
#################### POST ##############################
########################################################

@router.post("/admin", response_model=AdminOut)
def create_admin_user(admin: AdminCreate, db: Session = Depends(get_db)):
    admin_dict = admin.dict()
    admin_dict["hashed_password"] = "placeholder_password"
    db_admin = user_crud.create_admin(db, admin_dict)
    return db_admin
@router.post("/doctor", response_model=DoctorOut)
def create_doctor_user(doctor: DoctorCreate, db: Session = Depends(get_db)):
    doctor_dict = doctor.dict()
    doctor_dict["hashed_password"] = "placeholder_password"
    db_doctor = user_crud.create_doctor(db, doctor_dict)
    return db_doctor
@router.post("/nurse", response_model=NurseOut)
def create_nurse_user(nurse: NurseCreate, db: Session = Depends(get_db)):
    nurse_dict = nurse.dict()
    nurse_dict["hashed_password"] = "placeholder_password"
    db_nurse = user_crud.create_nurse(db, nurse_dict)
    return db_nurse
@router.post("/pharmacist", response_model=PharmacistOut)
def create_pharmacist_user(pharmacist: PharmacistCreate, db: Session = Depends(get_db)):
    pharmacist_dict = pharmacist.dict()
    pharmacist_dict["hashed_password"] = "placeholder_password"
    db_pharmacist = user_crud.create_pharmacist(db, pharmacist_dict)
    return db_pharmacist
@router.post("/physiotherapist", response_model=PhysiotherapistOut)
def create_physiotherapist_user(physiotherapist: PhysiotherapistCreate, db: Session = Depends(get_db)):
    physiotherapist_dict = physiotherapist.dict()
    physiotherapist_dict["hashed_password"] = "placeholder_password"
    db_physiotherapist = user_crud.create_physiotherapist(db, physiotherapist_dict)
    return db_physiotherapist
@router.post("/recreation", response_model=RecreationOut)
def create_recreation_user(recreation: RecreationCreate, db: Session = Depends(get_db)):
    recreation_dict = recreation.dict()
    recreation_dict["hashed_password"] = "placeholder_password"
    db_recreation = user_crud.create_recreation(db, recreation_dict)
    return db_recreation
@router.post("/patient", response_model=PatientOut)
def create_patient_user(patient: PatientCreate, db: Session = Depends(get_db)):
    patient_dict = patient.dict()
    patient_dict["hashed_password"] = "placeholder_password"
    db_patient = user_crud.create_patient(db, patient_dict)
    return db_patient

# @router.post("/", response_model=user_schema.UserRead)
# def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
#     return user_crud.create_user(db=db, user=user)

#######################################################
#################### GET ##############################
#######################################################

@router.get("/", response_model=List[UserOut])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return user_crud.get_users(db, skip=skip, limit=limit)

@router.get("/by-id/{user_id}", response_model=UserOut)
def read_user(user_id: int, db:Session = Depends(get_db)):
    db_user = user_crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/by-role/{role}", response_model=List[UserOut])
def get_by_role(role: UserRole, db: Session = Depends(get_db)):
    return user_crud.get_by_role(db, role)

@router.get("/by-firstname/{first_name}", response_model=List[UserOut])
def get_by_first_name(first_name: str, db: Session = Depends(get_db)):
    return user_crud.get_by_first_name(db, first_name)

#########################################################
#################### PATCH ##############################
#########################################################

@router.patch("/{user_id}", response_model=user_schema.UserRead)
def update_user(user_id: int, updates: user_schema.UserUpdate, db: Session = Depends(get_db)):
    db_user = user_crud.update_user(db, user_id=user_id, updates=updates)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.patch("/{user_id}/admin", response_model=user_schema.AdminUpdate)
def update_admin(user_id:int, admin_update: user_schema.AdminUpdate, db:Session = Depends(get_db)):
    updates = admin_update.dict(exclude_unset=True)
    user = user_crud.update_user(db, user_id, updates)
    if not user:
        raise HTTPException(status_code=404, detail="Admin not found")
    return user
    
@router.patch("/{user_id}/doctor", response_model=user_schema.DoctorUpdate)
def update_doctor(user_id: int, doctor_update: user_schema.DoctorUpdate, db: Session = Depends(get_db)):
    updates = doctor_update.dict(exclude_unset=True)
    user = user_crud.update_user(db, user_id, updates)
    if not user:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return user

@router.patch("/{user_id}/nurse", response_model=user_schema.NurseUpdate)
def update_nurse(user_id: int, nurse_update: user_schema.NurseUpdate, db: Session = Depends(get_db)):
    updates = nurse_update.dict(exclude_unset=True)
    user = user_crud.update_user(db, user_id, updates)
    if not user:
        raise HTTPException(status_code=404, detail="Nurse not found")
    return user

@router.patch("/{user_id}/pharmacist", response_model=user_schema.PharmacistUpdate)
def update_pharmacist(user_id: int, pharmacist_update: user_schema.PharmacistUpdate, db: Session = Depends(get_db)):
    updates = pharmacist_update.dict(exclude_unset=True)
    user = user_crud.update_user(db, user_id, updates)
    if not user:
        raise HTTPException(status_code=404, detail="Pharmacist not found")
    return user

@router.patch("/{user_id}/physiotherapist", response_model=user_schema.PhysiotherapistUpdate)
def update_physiotherapist(user_id: int, physiotherapist_update: user_schema.PhysiotherapistUpdate, db: Session = Depends(get_db)):
    updates = physiotherapist_update.dict(exclude_unset=True)
    user = user_crud.update_user(db, user_id, updates)
    if not user:
        raise HTTPException(status_code=404, detail="Physiotherapist not found")
    return user

@router.patch("/{user_id}/recreation", response_model=user_schema.RecreationUpdate)
def update_recreation(user_id: int, recreation_update: user_schema.RecreationUpdate, db: Session = Depends(get_db)):
    updates = recreation_update.dict(exclude_unset=True)
    user = user_crud.update_user(db, user_id, updates)
    if not user:
        raise HTTPException(status_code=404, detail="Recreation not found")
    return user

@router.patch("/{user_id}/patient", response_model=user_schema.PatientUpdate)
def update_patient(user_id: int, patient_update: user_schema.PatientUpdate, db: Session = Depends(get_db)):
    updates = patient_update.dict(exclude_unset=True)
    user = user_crud.update_user(db, user_id, updates)
    if not user:
        raise HTTPException(status_code=404, detail="Patient not found")
    return user


##########################################################
#################### DELETE ##############################
##########################################################

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, user_type: Optional[str] = None, db: Session = Depends(get_db)):
    db_user = user_crud.get_user(db, user_id)
    
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if user_type and db_user.type != user_type:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User is not of type {user_type}")
    
    user_crud.delete_user(db, db_user)
    return None # 204 No Content