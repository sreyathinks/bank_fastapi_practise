from sqlalchemy.orm import Session
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate
from app.models.account import Account
from fastapi import HTTPException

def create_transaction(db: Session, transaction: TransactionCreate):

    account = db.query(Account).filter(
        Account.id == transaction.account_id
    ).first()

    if transaction.transaction_type == "deposit":
        account.balance += transaction.amount

    elif transaction.transaction_type == "withdraw":
        if account.balance < transaction.amount:
            raise HTTPException(
             status_code=400,
             detail="Insufficient balance"
                    )

        account.balance -= transaction.amount

    db_transaction = Transaction(
        account_id=transaction.account_id,
        amount=transaction.amount,
        transaction_type=transaction.transaction_type,
        description=transaction.description
    )

    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)

    return db_transaction


def get_transaction(db: Session, transaction_id: int):

    return db.query(Transaction).filter(
        Transaction.id == transaction_id
    ).first()


def get_transactions(db: Session):

    return db.query(Transaction).all()


def update_transaction(
    db: Session,
    transaction_id: int,
    transaction: TransactionCreate
):

    db_transaction = db.query(Transaction).filter(
        Transaction.id == transaction_id
    ).first()

    if db_transaction:
        db_transaction.account_id = transaction.account_id
        db_transaction.amount = transaction.amount
        db_transaction.transaction_type = transaction.transaction_type
        db_transaction.description = transaction.description

        db.commit()
        db.refresh(db_transaction)

    return db_transaction


def delete_transaction(db: Session, transaction_id: int):

    db_transaction = db.query(Transaction).filter(
        Transaction.id == transaction_id
    ).first()

    if db_transaction:
        db.delete(db_transaction)
        db.commit()

    return db_transaction