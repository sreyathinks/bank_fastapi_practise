from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.database import SessionLocal
from app.schemas.customer import CustomerCreate, CustomerResponse
import app.services as services

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.post("/", response_model=CustomerResponse)
def add_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):
    return services.create_customer(db, customer)


@router.get("/{customer_id}", response_model=CustomerResponse)
def read_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    return services.get_customer(db, customer_id)


@router.get("/", response_model=list[CustomerResponse])
def read_customers(
    db: Session = Depends(get_db)
):
    return services.get_customers(db)


@router.put("/{customer_id}", response_model=CustomerResponse)
def edit_customer(
    customer_id: int,
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):
    return services.update_customer(db, customer_id, customer)


@router.delete("/{customer_id}")
def remove_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    services.delete_customer(db, customer_id)
    return {"message": "Customer deleted successfully"}