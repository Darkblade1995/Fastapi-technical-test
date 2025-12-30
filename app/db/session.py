from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Credenciales con el docker-compose  
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/technical_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

#  función en los endpoints para abrir/cerrar conexión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()