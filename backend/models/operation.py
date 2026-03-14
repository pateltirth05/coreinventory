from sqlalchemy import Column, Integer, String, ForeignKey
from database.db import Base


class Operation(Base):
    __tablename__ = "operations"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    status = Column(String)

    source_warehouse = Column(Integer, ForeignKey("warehouses.id"))
    destination_warehouse = Column(Integer, ForeignKey("warehouses.id"))
    supplier_name = Column(String, nullable=True)
    # it will do each inventory action like receipt delivery trnser and adjustment