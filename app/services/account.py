from sqlalchemy.orm import Session
from app.schemas.account import AccountCreate
from fastapi import HTTPException
import app.crud.account as cruds

def create_account(db:Session, account: AccountCreate):
    existing = cruds.get_by_account_number(db, account.account_number)

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Account already exists"
        )

    return cruds.create(db, account)

def get_account(db:Session, account_id: int):
    existing = cruds.get(db, account_id)

    if existing is None:
        raise HTTPException(
            status_code=404,
            detail="Account does not exist"
        )

    return existing

def get_accounts(db:Session):
    return cruds.gets(db)

def update_account(db:Session, account_id: int, account: AccountCreate):
    existing = cruds.get(db, account_id)

    if existing is None:
        raise HTTPException(
            status_code=404,
            detail="Account does not exist"
        )

    duplicate = cruds.get_by_account_number(
        db,
        account.account_number
    )

    if duplicate and duplicate.id != account_id:
        raise HTTPException(
            status_code=400,
            detail="Account number already exists"
        )

    return cruds.update(
        db,
        existing,
        account
    )

def delete_account(db:Session, account_id: int):
    existing = cruds.get(db, account_id)

    if existing is None:
        raise HTTPException(
            status_code=404,
            detail="Account does not exist"
        )

    cruds.delete(db, account_id)
    
