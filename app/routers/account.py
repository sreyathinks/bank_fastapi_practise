from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.account import AccountCreate, AccountResponse
from app.crud.account import (
    create_account,
    get_account,
    get_accounts,
    update_account,
    delete_account
)

router = APIRouter(
    prefix="/accounts",
    tags=["Accounts"]
)


@router.post("/", response_model=AccountResponse, summary="creates account")
def add_account(
    account: AccountCreate,
    db: Session = Depends(get_db)
):
    return create_account(db, account)


@router.get("/{account_id}", response_model=AccountResponse, summary="gets account by id")
def read_account(
    account_id: int,
    db: Session = Depends(get_db)
):
    return get_account(db, account_id)


@router.get("/", response_model=list[AccountResponse], summary="gets all accounts")
def read_accounts(
    db: Session = Depends(get_db)
):
    return get_accounts(db)


@router.put("/{account_id}", response_model=AccountResponse, summary="update account")
def edit_account(
    account_id: int,
    account: AccountCreate,
    db: Session = Depends(get_db)
):
    return update_account(db, account_id, account)


@router.delete("/{account_id}", summary="delete account")
def remove_account(
    account_id: int,
    db: Session = Depends(get_db)
):
    delete_account(db, account_id)
    return {"message": "Account deleted successfully"}