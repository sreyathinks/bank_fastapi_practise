from sqlalchemy.orm import Session
from app.models.account import Account
from app.schemas.account import AccountCreate


def create(db: Session, account: AccountCreate):

    db_account = Account(
        account_number=account.account_number,
        balance=account.balance,
        customer_id=account.customer_id
    )

    db.add(db_account)
    db.commit()
    db.refresh(db_account)

    return db_account


def get(db: Session, account_id: int):

    return db.query(Account).filter(
        Account.id == account_id
    ).first()


def gets(db: Session):

    return db.query(Account).all()


def update(db: Session, account_id: int, account: AccountCreate):

    db_account = db.query(Account).filter(
        Account.id == account_id
    ).first()

    if db_account:
        db_account.account_number = account.account_number
        db_account.balance = account.balance
        db_account.customer_id = account.customer_id

        db.commit()
        db.refresh(db_account)

    return db_account


def delete(db: Session, account_id: int):

    db_account = db.query(Account).filter(
        Account.id == account_id
    ).first()

    if db_account:
        db.delete(db_account)
        db.commit()

    return db_account