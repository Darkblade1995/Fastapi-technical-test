from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
import os

# Configuración básica
PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "Vulcano_es_la_onda" # Variables de entorno
ALGORITHM = "HS256"

def verify_password(plain_password, hashed_password):
    return PWD_CONTEXT.verify(plain_password, hashed_password)

def get_password_hash(password):
    return PWD_CONTEXT.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=30))
    to_encode.update({"exp": expire.timestamp()})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)