from sqlalchemy import Column, Integer, String, ForeignKey
from database.db import Base


class StockMovement(Base):
    __tablename__ = "stock_movements"

    id = Column(Integer, primary_key=True, index=True)

    product_id = Column(Integer, ForeignKey("products.id"))
    warehouse_id = Column(Integer, ForeignKey("warehouses.id"))
    operation_id = Column(Integer, ForeignKey("operations.id"))

    movement_type = Column(String)
    quantity = Column(Integer)
    # this is inventory ledger