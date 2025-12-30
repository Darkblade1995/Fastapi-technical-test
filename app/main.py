from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.tasks import router as tasks_router
from app.db.session import engine, Base, get_db
from app.models.models import User
from app.core.security import get_password_hash
from app.api.auth import router as auth_router

app = FastAPI(title="Aplicacion prueba tecnica - Backend")

app.include_router(tasks_router, prefix="/tasks", tags=["Tasks"])
app.include_router(auth_router, prefix="/auth", tags=["Autenticación"])

@app.on_event("startup")
def create_initial_user():
    db = SessionLocal()  
    try:
        user = db.query(User).filter(User.username == "admin").first()
        if not user:
            admin_user = User(
                username="admin",
                hashed_password=get_password_hash("admin123")
            )
            db.add(admin_user)
            db.commit()
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "API Funcional"}