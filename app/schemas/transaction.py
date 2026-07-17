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


class TransactionResponse(BaseModel):
    id: int
    account_id: int
    amount: float
    transaction_type: str
    description: str

    class Config:
        from_attributes = True