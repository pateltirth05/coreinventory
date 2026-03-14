from sqlalchemy import Column, Integer, String
from database.db import Base
# This file maps Python objects to the warehouses table in PostgreSQL.
class Warehouse(Base):
    __tablename__ = "warehouses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String)