from app.services.user_service import(create_user_service,  login_user_service)
from jose import jwt
import os

SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM="HS256"
def create_user_controller(user_data):
    return create_user_service(user_data)


def login_user_controller(email,password):
    user=login_user_service(email,password)
    if not user:
        return None
    payload={
        "user_id":str(user["_id"]),
        "email":user["email"]
    }
    token=jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
    return token