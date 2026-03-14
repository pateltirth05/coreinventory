from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.session import get_db
from services.operation_service import get_operations

router = APIRouter(prefix="/api/v1/operations", tags=["Operations"])


@router.get("/")
def operations(
    type: str | None = None,
    status: str | None = None,
    warehouse: int | None = None,
    db: Session = Depends(get_db)
):
    return get_operations(db, type, status, warehouse)