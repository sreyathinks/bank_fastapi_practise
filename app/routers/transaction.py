from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.schemas.transaction import (
    TransactionCreate,
    TransactionResponse
)
from app.crud.transaction import (
    create_transaction,
    get_transaction,
    get_transactions,
    update_transaction,
    delete_transaction
)

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=TransactionResponse)
def add_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db)
):
    return create_transaction(db, transaction)


@router.get("/{transaction_id}", response_model=TransactionResponse)
def read_transaction(
    transaction_id: int,
    db: Session = Depends(get_db)
):
    return get_transaction(db, transaction_id)


@router.get("/", response_model=list[TransactionResponse])
def read_transactions(
    db: Session = Depends(get_db)
):
    return get_transactions(db)


@router.put("/{transaction_id}", response_model=TransactionResponse)
def edit_transaction(
    transaction_id: int,
    transaction: TransactionCreate,
    db: Session = Depends(get_db)
):
    return update_transaction(db, transaction_id, transaction)


@router.delete("/{transaction_id}")
def remove_transaction(
    transaction_id: int,
    db: Session = Depends(get_db)
):
    delete_transaction(db, transaction_id)
    return {"message": "Transaction deleted successfully"}