from sqlalchemy.orm import Session
from app.models.customer import Customer
from app.schemas.customer import CustomerCreate

def create(db: Session, customer: CustomerCreate):

    db_customer = Customer(
        name=customer.name,
        email=customer.email,
        phone=customer.phone
    )

    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)

    return db_customer

def get_by_email(db: Session, email: str):
    return  (
        db.query(Customer)
        .filter(Customer.email == email)
        .first()
    )

def get(db: Session, customer_id: int):
    return db.query(Customer).filter(
        Customer.id == customer_id
    ).first()


def gets(db: Session):
    return db.query(Customer).all()


def update(db: Session, customer_id: int, customer: CustomerCreate):

    db_customer = db.query(Customer).filter(
        Customer.id == customer_id
    ).first()

    if db_customer:
        db_customer.name = customer.name
        db_customer.email = customer.email
        db_customer.phone = customer.phone

        db.commit()
        db.refresh(db_customer)

    return db_customer


def delete(db: Session, customer_id: int):

    db_customer = db.query(Customer).filter(
        Customer.id == customer_id
    ).first()

    if db_customer:
        db.delete(db_customer)
        db.commit()

    return db_customer