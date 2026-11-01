from app.services.user_service import(create_user_service,  login_user_service)

def create_user_controller(user_data):
    return create_user_service(user_data)


def login_user_controller(email,password):
    return login_user_service(email,password)