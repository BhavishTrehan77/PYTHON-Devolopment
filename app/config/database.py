import os
from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()

MONGO_URI=os.getenv("MONGO_URI")

client=MongoClient(MONGO_URI)
# here is the connection happening thorugh MONGOCLIENT

db=client["python_backend"]
# this is basically our database name

products_collection=db["products"]
# this is basicallt our collection name
users_collection = db["users"]
pdf_collection=db["pdf"]

try:
    client.admin.command("ping")
    print(" MONOGDB CONNECTED SUCCESSFULLY")
except Exception as e:
    print("MONGODB CONNECTION FAILED",e)

