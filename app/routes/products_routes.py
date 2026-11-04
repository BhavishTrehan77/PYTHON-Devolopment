from fastapi import APIRouter,Query,Depends,Request,UploadFile,File
from app.schemas.products_schema import ProductCreate, ProductUpdate,ProductResponse
from app.middleware.auth_middleware import auth_middleware
from app.controllers.product_controller import(
    create_product_controller,
    get_products_controller,
    get_product_by_id_controller,
    delete_product_controller,
    update_products_controller

)
from app.controllers.pdf_controller import save_pdf_controller,process_pdf_controller
from pypdf import PdfReader


import os


router=APIRouter()


@router.post("/create",response_model=ProductResponse,status_code=201)
def create_product(product:ProductCreate):
    return create_product_controller(product.model_dump())

@router.get("/")
def get_products(request:Request,limit: int=Query(default=10,ge=1,le=100),user=Depends(auth_middleware)):
    return get_products_controller(limit)

@router.get("/{product_id}",response_model=ProductResponse)

def get_product(product_id: str):
    return get_product_by_id_controller(product_id)

@router.delete("/{product_id}",response_model=ProductResponse)
def delete_product(product_id: str):
    return delete_product_controller(product_id)

@router.patch("/{product_id}")

def update_product(product_id: str,product:ProductUpdate):
    return update_products_controller(product_id,product.model_dump(exclude_unset=True))
@router.post("/upload")
async def upload_file(file:UploadFile=File(...)):
    os.makedirs("uploads",exist_ok=True)
    file_path=f"uploads/{file.filename}"
    contents=await file.read()
    with open(file_path,"wb") as f:
        f.write(contents)
    reader=PdfReader(file_path)
    text=""
    for page in reader.pages:
        text+=page.extract_text() or ""
    
    result=process_pdf_controller(text,file.filename)

    
    return{
        "message": "File uploaded successfully",
        "filename":file.filename,
        "content_type":file.content_type,
        "size":len(contents),
        "text":text,
        "database":result
    } 

