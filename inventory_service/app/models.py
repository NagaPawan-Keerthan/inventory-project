from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class InventoryItem(Base):
    """
    Database model for inventory items.
    """
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Item name
    quantity = Column(Integer, nullable=False)  # Item quantity
    price = Column(Numeric(10, 2), nullable=False)  # Item price

    def __repr__(self):
        return f"<InventoryItem(id={self.id}, name={self.name}, quantity={self.quantity}, price={self.price})>"