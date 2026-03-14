from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.session import get_db
from services.stock_service import get_stock

router = APIRouter(prefix="/api/v1/stock", tags=["Stock"])


@router.get("/")
def list_stock(db: Session = Depends(get_db)):
    return get_stock(db)


# here the endpoint created GET