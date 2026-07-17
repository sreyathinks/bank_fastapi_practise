from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.schemas.customer import CustomerCreate
import app.crud.customer as cruds


def create_customer(db: Session, customer: CustomerCreate):

    existing = cruds.get_by_email(db, customer.email)

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Customer already exists"
        )

    return cruds.create(db, customer)


def get_customer(db: Session, customer_id: int):

    customer = cruds.get(db, customer_id)

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer


def get_customers(db: Session):

    return cruds.gets(db)


def update_customer(
    db: Session,
    customer_id: int,
    customer: CustomerCreate
):

    existing = cruds.get(db, customer_id)

    if existing is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    duplicate = cruds.get_by_email(
        db,
        customer.email
    )

    if duplicate and duplicate.id != customer_id:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    return cruds.update(
        db,
        existing,
        customer
    )


def delete_customer(
    db: Session,
    customer_id: int
):

    existing = cruds.get(db, customer_id)

    if existing is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return cruds.delete(
        db,
        customer_id
    )