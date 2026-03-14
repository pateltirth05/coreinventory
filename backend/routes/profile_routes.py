from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from jose import jwt

from database.session import get_db
from services.profile_service import get_profile

SECRET_KEY = "inventory-secret"
ALGORITHM = "HS256"

router = APIRouter(prefix="/api/v1/profile", tags=["Profile"])


@router.get("/")
def profile(
    authorization: str = Header(None),
    db: Session = Depends(get_db)
):

    token = authorization.split(" ")[1]

    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    user_id = payload["user_id"]

    return get_profile(db, user_id)