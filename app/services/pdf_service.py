from app.config.database import pdf_collection
from app.services.chunking_service import chunk_text_by_words
from app.services.embedding_service import generate_embedding
def save_pdf_document(data):
    result=pdf_collection.insert_one(data)
    return{
        "id":str(result.inserted_id),
        "message":"pdf text stored successfully"
    }

def process_pdf(text,filename):
    chunks=chunk_text_by_words(text,TextSize=500,overlap=50)
    documents=[]
    for chunk in chunks:
        embedding=generate_embedding(chunk)
        documents.append({
            "text":chunk,
            "embedding":embedding,
            "metadata":{
                "source":filename
            }
        })
    if documents:
        result=pdf_collection.insert_many(documents)
        return{
            "message":"PDF EMBEDDED ARE STORED SUCCESS",
            "chunks": len(result.inserted_ids)
        }
    return{
        "message":"NO TEXT FOUND",
        "chunks":0
    }