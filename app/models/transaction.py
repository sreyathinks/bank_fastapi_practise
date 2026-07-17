from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime, func
from app.core.database import Base




class Transaction(Base):


    __tablename__ = "transactions"


    id = Column(Integer, primary_key=True, index=True)


    account_id = Column(
        Integer,
        ForeignKey("accounts.id")
    )


    amount = Column(Float)


    transaction_type = Column(String)


    description = Column(String)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
