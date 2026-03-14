from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "inventory-secret"
ALGORITHM = "HS256"


def create_access_token(data: dict):

    payload = data.copy()
    expire = datetime.utcnow() + timedelta(hours=12)

    payload.update({"exp": expire})

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return token