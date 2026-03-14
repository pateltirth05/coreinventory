from models.user import User
from services.auth_utils import hash_password, verify_password
from services.jwt_service import create_access_token


def signup_user(db, user_data):

    user = User(
        name=user_data.name,
        email=user_data.email,
        password=hash_password(user_data.password)
    )

    db.add(user)
    db.commit()

    return {"message": "User created"}


def login_user(db, login_data):

    user = db.query(User).filter(User.email == login_data.email).first()

    if not user:
        raise Exception("Invalid credentials")

    if not verify_password(login_data.password, user.password):
        raise Exception("Invalid credentials")

    token = create_access_token({"user_id": user.id})

    return {"access_token": token}