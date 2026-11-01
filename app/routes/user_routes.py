from fastapi import APIRouter,HTTPException

from app.controllers.user_controller import(create_user_controller,login_user_controller)

from app.schemas.user_schema import(SignupSchema,LoginSchema)

router=APIRouter()


@router.post("/signup")
def create_router(user:SignupSchema):
    user_id= create_user_controller(user.model_dump())
    return{
        "message":"user created success",
        "user_id":user_id
    }

@router.post("/login")

def login_router(user:LoginSchema):
    exisitng_user=login_user_controller(user.email,user.password)
    if not existing_user:
        raise HTTPException( status_code=401,
            detail="Invalid email or password")
    return{
        "message":"user found"
    }



