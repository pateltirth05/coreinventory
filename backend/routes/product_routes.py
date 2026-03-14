from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.product_schema import ProductCreate
from services.product_service import create_product
from database.session import get_db

from services.product_service import search_products

from schemas.product_schema import ProductUpdate
from services.product_service import update_product
router = APIRouter(prefix="/api/v1/products", tags=["Products"])

@router.post("/")
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

@router.get("/search")
def search(keyword: str, db: Session = Depends(get_db)):
    return search_products(db, keyword)



@router.put("/{product_id}")
def update(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    return update_product(db, product_id, product)