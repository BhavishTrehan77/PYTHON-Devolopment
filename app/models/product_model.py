from app.config.database import products_collection
from bson import ObjectId

def create_product(product_data):
    result=products_collection.insert_one(product_data)
    return str(result.inserted_id)

def get_products(limit):
    products = list(products_collection.find().limit(limit))
    for product in products:
        product["_id"] = str(product["_id"])
    return products


def get_products_by_id(product_id):
    product= products_collection.find_one({"_id":  ObjectId(product_id)})
    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    product["_id"]=str(product["_id"])
    return product




def delete_products(product_id):
    result= products_collection.delete_one({"_id": ObjectId(product_id)})
    return result.deleted_count
    

def update_products(product_id,update_data):
    result=products_collection.update_one({"_id":ObjectId(product_id)},{"$set":update_data})
    return result.modified_count