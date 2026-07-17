# BANKPRACT

A backend banking application built using **FastAPI**, following a modular architecture with separate layers for configuration, database management, models, schemas, CRUD operations, and API routers.

## Project Structure

```
BANKPRACT/
│
├── alembic/               # Database migration scripts
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── app/
│   ├── core/              # Application configuration and database setup
│   │   ├── config.py
│   │   └── database.py
│   │
│   ├── crud/              # Database operations
│   │   ├── account.py
│   │   ├── customer.py
│   │   └── transaction.py
│   │
│   ├── models/            # SQLAlchemy models
│   │
│   ├── routers/           # API endpoints
│   │   ├── account.py
│   │   ├── customer.py
│   │   └── transaction.py
│   │
│   ├── schemas/           # Pydantic request and response models
│   │   ├── account.py
│   │   ├── customer.py
│   │   └── transaction.py
│   │
│   └── main.py            # FastAPI application entry point
│
├── .gitignore
├── alembic.ini
├── requirements.txt
└── README.md
```

## Technology Stack

- Python
- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- Pydantic

## Architecture

The project follows a layered architecture:

- **core** – Application configuration and database connection.
- **models** – Database table definitions.
- **schemas** – Request and response validation using Pydantic.
- **crud** – Business logic and database operations.
- **routers** – REST API endpoints.
- **alembic** – Database schema versioning and migrations.


### Run the project

```bash
uvicorn app.main:app --reload