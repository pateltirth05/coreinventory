from sqlalchemy import Column, Integer, ForeignKey
from database.db import Base
# This represents inventory quantity per warehouse.
class Stock(Base):
    __tablename__ = "stock"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    warehouse_id = Column(Integer, ForeignKey("warehouses.id"))
    quantity = Column(Integer, default=0)