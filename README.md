# Prueba Técnica - FastAPI Task API

## Descripción
API REST funcional para la gestión de tareas con autenticación JWT y persistencia en PostgreSQL.

## Tecnologías
* Python 3.11.8 / 3.13
* FastAPI
* SQLAlchemy
* Docker (PostgreSQL)

## Instrucciones de Ejecución
1. Levantar la base de datos: `docker-compose up -d`
2. Instalar dependencias: `pip install -r requirements.txt`
3. Iniciar la aplicación: `uvicorn app.main:app --reload`

## Credenciales del Usuario Inicial
* **Usuario:** admin
* **Contraseña:** admin123

## Decisiones Técnicas
* Se implementaron índices en `id` y `title` de la tabla de tareas para optimizar el rendimiento de las búsquedas.
* La arquitectura es modular para facilitar la escalabilidad.