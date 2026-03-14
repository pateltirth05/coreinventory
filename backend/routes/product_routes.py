from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.product_schema import ProductCreate
from services.product_service import create_product
from database.session import get_db

router = APIRouter(prefix="/api/v1/products", tags=["Products"])

@router.post("/")
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)