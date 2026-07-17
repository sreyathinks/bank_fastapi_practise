from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.database import SessionLocal
from app.schemas.transaction import (
    TransactionCreate,
    TransactionResponse
)
import app.services as services

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

@router.post("/", response_model=TransactionResponse)
def add_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db)
):
    return services.create_transaction(db, transaction)


@router.get("/{transaction_id}", response_model=TransactionResponse)
def read_transaction(
    transaction_id: int,
    db: Session = Depends(get_db)
):
    return services.get_transaction(db, transaction_id)


@router.get("/", response_model=list[TransactionResponse])
def read_transactions(
    db: Session = Depends(get_db)
):
    return services.get_transactions(db)


@router.put("/{transaction_id}", response_model=TransactionResponse)
def edit_transaction(
    transaction_id: int,
    transaction: TransactionCreate,
    db: Session = Depends(get_db)
):
    return services.update_transaction(db, transaction_id, transaction)


@router.delete("/{transaction_id}")
def remove_transaction(
    transaction_id: int,
    db: Session = Depends(get_db)
):
    services.delete_transaction(db, transaction_id)
    return {"message": "Transaction deleted successfully"}