from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.session import get_db
from services.profile_service import get_profile

router = APIRouter(prefix="/api/v1/profile", tags=["Profile"])


@router.get("/")
def profile(db: Session = Depends(get_db)):
    # for hackathon we return first user
    return get_profile(db, 1)