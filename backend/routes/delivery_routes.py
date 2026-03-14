from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.session import get_db
from schemas.delivery_schema import DeliveryCreate
from services.delivery_service import create_delivery

router = APIRouter(prefix="/api/v1/deliveries", tags=["Deliveries"])


@router.post("/")
def add_delivery(delivery: DeliveryCreate, db: Session = Depends(get_db)):
    return create_delivery(db, delivery)