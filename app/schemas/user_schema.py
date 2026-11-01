from pydantic import BaseModel,Field,EmailStr

class SignupSchema(BaseModel):
    name:str=Field(min_length=3)
    email:EmailStr
    password: str=Field(min_length=6)

class LoginSchema(BaseModel):
    email:EmailStr
    password:str=Field(min_length=6)
    