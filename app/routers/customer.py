from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.database import SessionLocal
from app.schemas.customer import CustomerCreate, CustomerResponse
from app.crud.customer import (
    create_customer,
    get_customer,
    get_customers,
    update_customer,
    delete_customer
)

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.post("/", response_model=CustomerResponse)
def add_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):
    return create_customer(db, customer)


@router.get("/{customer_id}", response_model=CustomerResponse)
def read_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    return get_customer(db, customer_id)


@router.get("/", response_model=list[CustomerResponse])
def read_customers(
    db: Session = Depends(get_db)
):
    return get_customers(db)


@router.put("/{customer_id}", response_model=CustomerResponse)
def edit_customer(
    customer_id: int,
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):
    return update_customer(db, customer_id, customer)


@router.delete("/{customer_id}")
def remove_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    delete_customer(db, customer_id)
    return {"message": "Customer deleted successfully"}