from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.session import get_db
from schemas.transfer_schema import TransferCreate
from services.transfer_service import create_transfer

router = APIRouter(prefix="/api/v1/transfers", tags=["Transfers"])

@router.post("/")
def add_transfer(transfer: TransferCreate, db: Session = Depends(get_db)):
    return create_transfer(db, transfer)