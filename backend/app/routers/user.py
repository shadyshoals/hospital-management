from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.crud import user as user_crud
from app.schemas import user as user_schema
from app.database import get_db

router = APIRouter(prefix="/users", tags=["users"])

# POST
@router.post("/", response_model=user_schema.UserRead)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    return user_crud.create_user(db=db, user=user)

# GET
@router.get("/", response_model=List[user_schema.UserRead])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return user_crud.get_users(db, skip=skip, limit=limit)

@router.get("/{user_id}", response_model=user_schema.UserRead)
def read_user(user_id: int, db:Session = Depends(get_db)):
    db_user = user_crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# PATCH
@router.patch("/{user_id}", response_model=user_schema.UserRead)
def update_user(user_id: int, updates: user_schema.UserUpdate, db: Session = Depends(get_db)):
    db_user = user_crud.update_user(db, user_id=user_id, updates=updates)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# DELETE
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    success = user_crud.delete_user(db, user_id=user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"ok": True}
