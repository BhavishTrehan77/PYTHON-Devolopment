from app.models.product_model import (
    create_product,
    get_products,
    get_products_by_id,
    delete_products,
    update_products
)


def create_product_service(product_data):
    return create_product(product_data)


def get_products_service():
    return get_products()


def get_products_by_id_service(product_id):
    return get_products_by_id(product_id)


def delete_product_service(product_id):
    return delete_products(product_id)

def update_products_service(product_id,product_data):
    return update_products(product_id,product_data)
    