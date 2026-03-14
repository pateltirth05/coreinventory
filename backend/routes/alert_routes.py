from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.session import get_db
from services.alert_service import get_low_stock_products

router = APIRouter(prefix="/api/v1/alerts", tags=["Alerts"])


@router.get("/low-stock")
def low_stock_alerts(db: Session = Depends(get_db)):
    return get_low_stock_products(db)