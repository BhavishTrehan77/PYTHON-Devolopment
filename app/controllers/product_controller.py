from app.services.product_service import (
    create_product_service,
    get_products_service,
    get_products_by_id_service,
    delete_product_service,
    update_products_service
)

def create_product_controller(product_data):
    return create_product_service(product_data)

def get_products_controller(limit):
    return get_products_service(limit)


def get_product_by_id_controller(product_id):
    return get_products_by_id_service(product_id)

def delete_product_controller(product_id):
    return delete_product_service(product_id)

def update_products_controller(product_id,product_data):
    return update_products_service(product_id,product_data)
