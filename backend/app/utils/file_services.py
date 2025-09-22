import os, shutil
from dotenv import load_dotenv
from uuid import uuid4

from fastapi import Depends
from pytest import Session

from app.crud import user as user_crud
from app.crud import medical_history as medical_history_crud
from fpdf import FPDF
from pypdf import PdfWriter, PdfReader
from datetime import datetime, timezone

from app.database import get_db

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


def merge_pdfs(pdf_list, output_path):
    writer = PdfWriter()
    for pdf_path in pdf_list:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            writer.add_page(page)
    with open(output_path, "wb") as f:
        writer.write(f)

def generate_pdf_patient(patient_id: int, db: Session = Depends(get_db)):
    #output: first_last_datetime_of_create

    # 1 Get patient object
    db_user = user_crud.get_user(db, patient_id)
    # 2 Check if usre none

    # 3 Get all medical records of that user
    db_medical_records = medical_history_crud.get_by_patient(db, patient_id)
    # 4 Check if empty list

    # 5 Create PDF
    

    pdf = FPDF()
    usable_width = pdf.w - 2 * pdf.l_margin
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)

    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(200, 10, "Patient Medical Summary", ln=True, align="C")
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())

    # - Patient Info
    pdf.set_font("Helvetica", size=12)
    pdf.cell(0, 10, f"Name: {db_user.first_name} {db_user.last_name}", ln=True)
    pdf.cell(0, 10, f"DOB: TO BE ADDED", ln=True)
    pdf.cell(0, 10, f"Patient ID: {db_user.id}", ln=True)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())

    # - Medical history info
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 10, "Medical History:", ln=True)
    pdf.set_font("Helvetica", size=12)

    for record in db_medical_records:
        # todo: fix the datetime format
        pdf.multi_cell(usable_width, 10, f"- Date: {record.created_at}\n"
                       f"   Notes: {record.notes or 'No notes'}\n"
                       f"   Uploaded by: TO BE ADDED"
        )
        pdf.ln(2) 
        pdf.set_x(pdf.l_margin) 
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())

    summary_path = "summary_temp.pdf"
    pdf.output(summary_path)

    # todo: reorder the pdfs to be inserted after the proper corresponding medical record, rather than at the end?? maybe not

    my_pdf_list = [summary_path]
    for record in db_medical_records:
        ext = os.path.splitext(record.document_path)[1]
        if record.document_path:
            my_pdf_list.append(record.document_path)


    current_datetime = datetime.now(timezone.utc).isoformat()
    output_path = f"{db_user.first_name}_{db_user.last_name}_{current_datetime}.pdf"

    merge_pdfs(my_pdf_list, output_path)
               
    os.remove(summary_path)

    return output_path

## todo: option to generate pdf of individual medical record rather than all at once
#def generate_pdf_medical_record(medical_record_id: int):

