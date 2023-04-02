from pydantic import BaseModel
from models.models import Document
from typing import List, Optional


class UpsertRequest(BaseModel):
    documents: List[Document]


class UpsertResponse(BaseModel):
    ids: List[str]


class QuestionRequest(BaseModel):
    question: str


class QuestionResponse(BaseModel):
    answer: str


class DeleteRequest(BaseModel):
    ids: Optional[List[str]] = None
    delete_all: Optional[bool] = False


class DeleteResponse(BaseModel):
    success: bool
