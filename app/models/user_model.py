from app.config.database import users_collection


def create_user(user_data):
    result= users_collection.insert_one(user_data)
    return str(result.inserted_id)


def get_user_by_email(email):
    return users_collection.find_one({"email":email})
