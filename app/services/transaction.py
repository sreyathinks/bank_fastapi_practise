from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.schemas.transaction import TransactionCreate

import app.crud.transaction as transaction_crud
import app.crud.account as account_crud

def create_transaction(
    db: Session,
    transaction: TransactionCreate
):

    account = account_crud.get(
        db,
        transaction.account_id
    )

    if account is None:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )

    if transaction.transaction_type == "deposit":

        account.balance += transaction.amount

    elif transaction.transaction_type == "withdraw":

        if account.balance < transaction.amount:
            raise HTTPException(
                status_code=400,
                detail="Insufficient balance"
            )

        account.balance -= transaction.amount

    else:
        raise HTTPException(
            status_code=400,
            detail="Invalid transaction type"
        )

    db.commit()

    return transaction_crud.create(
        db,
        transaction
    )

def get_transaction(
    db: Session,
    transaction_id: int
):

    transaction = transaction_crud.get(
        db,
        transaction_id
    )

    if transaction is None:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    return transaction

def get_transactions(db: Session):

    return transaction_crud.gets(db)

def get_account_transactions(
    db: Session,
    account_id: int
):

    account = account_crud.get(
        db,
        account_id
    )

    if account is None:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )

    return transaction_crud.get_by_account_id(
        db,
        account_id
    )

    