from pydantic import BaseModel
from typing import Optional

class PDFMetadata(BaseModel):
    source:str
class PDFDocument(BaseModel):
    text: str
    embedding: list[float]
    metadata: dict