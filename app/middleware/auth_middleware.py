from fastapi import Request,HTTPException
from jose import jwt,JWTError
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM="HS256"


def auth_middleware(request:Request):
    auth_header=request.headers.get("Authorization")
    if not auth_header:
        raise HTTPException(
            status_code=401,
            detail="Authorization header missing"
        )
    try:
        schema,token=auth_header.split(" ")
        if schema.lower()!="bearer":
            raise HTTPException(
                status_code=401,
                detail="Invalid authentication schema"
            )
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        request.state.user=payload
        return payload
    except(JWTError,ValueError):
        raise HTTPException(
            status_code=401,
            detail="Invalid or Expired token"
        )
