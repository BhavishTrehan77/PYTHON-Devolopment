from fastapi import FastAPI

from app.routes.products_routes import router as product_router
from app.routes.user_routes import router as user_router

app = FastAPI()

app.include_router(product_router, prefix="/products")
app.include_router(user_router, prefix="/api")
print("OPENAPI PATHS:", list(app.openapi()["paths"].keys()))