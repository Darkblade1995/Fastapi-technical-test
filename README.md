# Technical Assessment – FastAPI Task API

**Author:** Luis Fernando Agamez Atehortua 
**Role:** Software Engineer  

---

## Description
A functional REST API for task management with JWT authentication and PostgreSQL persistence.

## Technologies
- Python 3.11.8 / 3.13
- FastAPI
- SQLAlchemy
- Docker (PostgreSQL)

## Execution Instructions
1. Start the database:
   ```bash
   docker-compose up -d
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
uvicorn app.main:app --reload
Initial User Credentials
Username: admin

Password: admin123

Technical Decisions
Indexes were implemented on the id and title columns of the tasks table to optimize search performance.

A modular architecture was adopted to facilitate scalability and future maintenance.
