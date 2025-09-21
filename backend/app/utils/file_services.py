import os, shutil
from dotenv import load_dotenv
from uuid import uuid4

load_dotenv()
UPLOAD_DIR = os.getenv("UPLOAD_DIR")
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_uploaded_file(patient_id: int, file) -> str:
    unique_filename = uuid4()
    ext = os.path.splitext(file.filename)[1]
    file_path = os.path.join(UPLOAD_DIR,f"{unique_filename}{ext}")
    # file_path = os.path.join(UPLOAD_DIR,f"{patient_id}_{file.filename}")
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return file_path