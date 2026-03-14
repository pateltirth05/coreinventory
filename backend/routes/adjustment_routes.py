from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.session import get_db
from schemas.adjustment_schema import AdjustmentCreate
from services.adjustment_service import create_adjustment

router = APIRouter(prefix="/api/v1/adjustments", tags=["Adjustments"])


@router.post("/")
def add_adjustment(adjustment: AdjustmentCreate, db: Session = Depends(get_db)):
    return create_adjustment(db, adjustment)