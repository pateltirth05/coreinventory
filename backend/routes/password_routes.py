from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.session import get_db
from services.otp_service import generate_otp, verify_otp
from services.auth_service import reset_password

router = APIRouter(prefix="/api/v1/password", tags=["Password Reset"])


@router.post("/request-otp")
def request_otp(email: str):

    otp = generate_otp(email)

    return {
        "message": "OTP generated",
        "otp": otp
    }


@router.post("/verify-otp")
def verify(email: str, otp: int):

    valid = verify_otp(email, otp)

    if not valid:
        raise Exception("Invalid OTP")

    return {"message": "OTP verified"}


@router.post("/reset")
def reset(email: str, new_password: str, db: Session = Depends(get_db)):

    return reset_password(db, email, new_password)