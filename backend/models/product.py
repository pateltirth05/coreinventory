from sqlalchemy import Column, Integer, String
from database.db import Base
# This maps to the products table you already created in PostgreSQL.
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    sku = Column(String, unique=True)
    category = Column(String)
    unit = Column(String)
    reorder_level = Column(Integer)