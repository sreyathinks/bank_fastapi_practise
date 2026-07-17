from pydantic import BaseModel


class AccountCreate(BaseModel):
    account_number: str
    balance: float
    customer_id: int


class AccountResponse(BaseModel):
    id: int
    account_number: str
    balance: float
    customer_id: int

    class Config:
        from_attributes = True