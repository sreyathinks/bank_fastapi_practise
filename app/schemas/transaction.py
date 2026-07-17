from pydantic import BaseModel
from enum import Enum

class TransactionType(str, Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
class TransactionCreate(BaseModel):
    account_id: int
    amount: float
    transaction_type: TransactionType
    description: str

class TransactionResponse(TransactionCreate):
    id: int

    class Config:
        from_attributes = True