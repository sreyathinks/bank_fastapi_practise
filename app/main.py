from fastapi import FastAPI

from app.routers import customer
from app.routers import account
from app.routers import transaction

app = FastAPI()

app.include_router(customer.router)
app.include_router(account.router)
app.include_router(transaction.router)