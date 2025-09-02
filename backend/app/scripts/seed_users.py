from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app.models.user import User, UserRole
from app.security import get_password_hash  # optional, if you hash passwords

# Create tables if they don't exist (safe if Alembic already ran)
Base.metadata.create_all(bind=engine)

# Open a session
db: Session = SessionLocal()

# Define seed users
seed_users = [
    {"username": "bbababab333abaliddddce", "first_name": "Aledabdseeice", "last_name": "Smadsfiteeeh", "role": "recreation manager", "password": "alic33e123"},
    {"username": "babababa33odddb", "first_name": "Boeedabsbseeb", "last_name": "Johnfdsadseeeon", "role": "psw", "password": "bob33123"},
    {"username": "cadabababadddbdddrol", "first_name": "Careeasbasdbaeeol", "last_name": "Leeeeebsasee", "role": "nurse manager", "password": "car33ol123"},
]

# Insert users
for u in seed_users:
    hashed_password = get_password_hash(u["password"])
    user = User(
        username=u["username"],
        first_name=u["first_name"],
        last_name=u["last_name"],
        role=UserRole(u["role"]),
        hashed_password=hashed_password
    )
    db.add(user)

db.commit()
print("Seeded users successfully.")
db.close()