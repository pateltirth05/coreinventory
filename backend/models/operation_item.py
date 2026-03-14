from sqlalchemy import Column, Integer, ForeignKey
from database.db import Base


class OperationItem(Base):
    __tablename__ = "operation_items"

    id = Column(Integer, primary_key=True, index=True)

    operation_id = Column(Integer, ForeignKey("operations.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    quantity = Column(Integer)
    # one receipt can contains multiple product