from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.session import get_db
from schemas.receipt_schema import ReceiptCreate
from services.receipt_service import create_receipt

router = APIRouter(prefix="/api/v1/receipts", tags=["Receipts"])


@router.post("/")
def add_receipt(receipt: ReceiptCreate, db: Session = Depends(get_db)):
    return create_receipt(db, receipt)