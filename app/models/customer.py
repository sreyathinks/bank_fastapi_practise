from sqlalchemy import Column, Integer, String, DateTime, func, Boolean
from app.core.database import Base


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    #phone= Column(String)
    address = Column(String)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    deleted_at = Column(DateTime, nullable=True)

    is_deleted = Column(Boolean, default=False)
