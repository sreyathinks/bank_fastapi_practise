from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.core.database import Base


class Account(Base):


    __tablename__="accounts"


    id = Column(Integer, primary_key=True)


    account_number = Column(String)


    balance = Column(Integer)


    customer_id = Column(
        Integer,
        ForeignKey("customers.id")
    )
