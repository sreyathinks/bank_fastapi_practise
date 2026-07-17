from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func, Boolean
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

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    deleted_at = Column(DateTime, nullable=True)

    is_deleted = Column(Boolean, default=False)
