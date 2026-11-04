from fastapi import APIRouter
from app.controllers.retrieval_controller import rag_ret_controller

router=APIRouter()


@router.get("/search")
def search_context(query:str):
    results=rag_ret_controller(query)
    return{
        "query":query,
        "results":results,

    }