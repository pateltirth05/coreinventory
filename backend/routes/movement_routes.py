from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.session import get_db
from services.movement_service import get_movements

router = APIRouter(prefix="/api/v1/movements", tags=["Move History"])


@router.get("/")
def movement_history(db: Session = Depends(get_db)):
    return get_movements(db)