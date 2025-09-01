# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import patient, appointment

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://localhost:5173"], # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(patient.router)
app.include_router(appointment.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the hospital management system!"}

@app.get("/health")
def read_route_health():
    return {"status":"ok"}