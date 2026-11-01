from fastapi import Depends,HTTPException
from app.middleware.auth_middleware import auth_middleware


def AuthMiddleware(user=Depends(auth_middleware)):
    if(user["role"]!="admin"):
        raise HTTPException(status_code=403,detail="admin access required")
    return user