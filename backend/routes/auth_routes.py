from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.session import get_db
from schemas.auth_schema import UserSignup, UserLogin
from services.auth_service import signup_user, login_user

router = APIRouter(prefix="/api/v1/auth", tags=["Authentication"])


@router.post("/signup")
def signup(user: UserSignup, db: Session = Depends(get_db)):
    return signup_user(db, user)


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return login_user(db, user)