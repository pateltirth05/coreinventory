from models.user import User


def get_profile(db, user_id):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise Exception("User not found")

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "role": user.role
    }