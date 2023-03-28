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
    created_at: Optional[str]
    author: Optional[str]


class Document(BaseModel):
    id: Optional[str] = None
    text: str
    metadata: DocumentMetadata


class Query(BaseModel):
    query: str


class QueryWithEmbedding(Query):
    embedding: List[float]


class QueryResult(BaseModel):
    query: str
    results: List[DocumentChunk]
