from pydantic import BaseModel
from typing import Optional, List


class DocumentChunkMetadata(BaseModel):
    document_id: Optional[str] = None


class DocumentChunk(BaseModel):
    id: Optional[str] = None
    text: str
    metadata: DocumentChunkMetadata
    embedding: Optional[List[float]] = None


class DocumentChunkWithScore(DocumentChunk):
    score: float


class DocumentMetadata(BaseModel):
    title: Optional[str]
    author: Optional[str]
    created_at: Optional[str]
    file_type: Optional[str]


class Document(BaseModel):
    id: Optional[str] = None
    text: str
    metadata: DocumentMetadata


class Question(BaseModel):
    question: str


class QuestionWithEmbedding(Question):
    embedding: List[float]


class Answer(BaseModel):
    question: Question
    results: List[DocumentChunkWithScore]
