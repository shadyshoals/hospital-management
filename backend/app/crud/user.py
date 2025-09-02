from sqlalchemy.orm import Session
from app import models
from app.schemas import user as user_schema
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(db:Session, user_id: int):
    return db.query(models.user.User).filter(models.user.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.user.User).offset(skip).limit(limit).all()

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

def update_user(db: Session, user_id: int, updates: user_schema.UserUpdate):
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    for key, value in updates.dict(exclude_unset=True).items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db:Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    return False