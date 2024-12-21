from sqlalchemy import Column, Integer, String, JSON, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Order(Base):
    """
    Database model for orders.
    """
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String, default="Pending")  # Order status
    items = Column(JSON, nullable=False)  # List of item names
    total_price = Column(Numeric(10, 2), nullable=False)  # Total price of the order

    def __repr__(self):
        return f"<Order(id={self.id}, status={self.status}, items={self.items}, total_price={self.total_price})>"