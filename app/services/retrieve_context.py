from app.config.database import pdf_collection
from app.services.embedding_service import generate_embedding
from dotenv import load_dotenv
from google import genai
import os

load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
def ragRet(query,limit=5):
    embedding=generate_embedding(query)
    results=pdf_collection.aggregate([
        {
            "$vectorSearch":{
                "index":"vector_index",
                "path":"embedding",
                "queryVector":embedding,
                "numCandidates":50,
                "limit":limit
            }
        },{
            "$project":{
                "_id":0,
                "text":1,
                "metadata":1,
                "score":{
                    "$meta":"vectorSearchScore"
                }
            }
        }
    ])
    
    results= list(results)
    context="\n\n".join(
        result["text"]
        for result in results
    )
    prompt=f"""
    Answer the question using only the provided context If the answer is not present in the context,
    say that you could not find the answer in the provided documents.

    Content:
    {context}

    Question:
    {query}
    """
    response=client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )
    return{
        "answer":response.text,
        "sources":results
    }