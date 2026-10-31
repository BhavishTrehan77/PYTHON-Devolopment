from fastapi import APIRouter
from app.schemas.products_schema import ProductCreate, ProductUpdate

from app.controllers.product_controller import(
    create_product_controller,
    get_products_controller,
    get_product_by_id_controller,
    delete_product_controller,
    update_products_controller

)

router=APIRouter()


@router.post("/create")
def create_product(product:ProductCreate):
    return create_product_controller(product.model_dump())

@router.get("/")
def get_products():
    return get_products_controller()

@router.get("/{product_id}")

def get_product(product_id: str):
    return get_product_by_id_controller(product_id)

@router.delete("/{product_id}")
def delete_product(product_id: str):
    return delete_product_controller(product_id)

@router.patch("/{product_id}")

def update_product(product_id: str,product:ProductUpdate):
    return update_products_controller(product_id,product.model_dump(exclude_unset=True))
