from app.models.user_model import(create_user,get_user_by_email)
from app.utils.sec import hash_password,verify_password

def create_user_service(user_data):
    user_data["password"]=hash_password(user_data["password"])
    return create_user(user_data)

def login_user_service(email,password):
    user= get_user_by_email(email)
    if not user:
        return None
    Is_Match=verify_password(password,user["password"])
    if not Is_Match:
        return None
    return user