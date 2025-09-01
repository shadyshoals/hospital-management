from app.database import SessionLocal
from app.models.user import User
from datetime import datetime, timezone
from passlib.context import CryptContext

#password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

db = SessionLocal()

users_to_create = [
    User(
        first_name="Alice", 
        last_name="Smith", 
        username="alice",
        hashed_password=hash_password("password123"),
        role="doctor", 
        created_at=datetime.now(timezone.utc)
    ),
    User(
        first_name="Bob", 
        last_name="Johnson", 
        username="bob",
        hashed_password=hash_password("password123"),
        role="doctor", 
        created_at=datetime.now(timezone.utc)
    ),
    User(
        first_name="Carol", 
        last_name="Lee", 
        username="carol",
        hashed_password=hash_password("password123"),
        role="admin", 
        created_at=datetime.now(timezone.utc)
    ),
]

for user in users_to_create:
    db.add(user)

db.commit()
db.close()

print("Seeded users successfully")