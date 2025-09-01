from app.database import Base, engine
from app.models import User, Patient

Base.metadata.create_all(bind=engine)