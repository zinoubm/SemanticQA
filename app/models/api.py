from pydantic import BaseModel
from models.models import Document
from typing import List


class UpsertRequest(BaseModel):
    documents: List[Document]


class UpsertResponse(BaseModel):
    ids: List[str]


class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    result: str
