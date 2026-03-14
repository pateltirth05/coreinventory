from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.session import get_db
from schemas.warehouse_schema import WarehouseCreate
from services.warehouse_service import create_warehouse, get_warehouses

router = APIRouter(prefix="/api/v1/warehouses", tags=["Warehouses"])

# this will create API endpoints
@router.post("/")
def add_warehouse(warehouse: WarehouseCreate, db: Session = Depends(get_db)):
    return create_warehouse(db, warehouse)


@router.get("/")
def list_warehouses(db: Session = Depends(get_db)):
    return get_warehouses(db)