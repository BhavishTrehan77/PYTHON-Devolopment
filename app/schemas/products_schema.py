from typing import Optional
from pydantic import BaseModel,Field

class ProductCreate(BaseModel):
    name:str=Field(min_length=3)
    price:float=Field(ge=0)
    quantity:int=Field(ge=1)
    description:Optional[str]=None



class ProductUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=3)
    price: Optional[float] = Field(default=None, ge=0)
    quantity: Optional[int] = Field(default=None, ge=1)
    description: Optional[str] = None

class ProductResponse(BaseModel):
    id:str
    name:str
    price: int
    quantity: int
    description: str