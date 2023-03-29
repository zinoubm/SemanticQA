import os
from qdrant_client import QdrantClient
from qdrant_client.http import models

import openai

COLLECTION_NAME = os.getenv("COLLECTION_NAME")
QDRANT_PORT = os.getenv("QDRANT_PORT")
QDRANT_HOST = os.getenv("QDRANT_HOST")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY


def get_embedding(input: str):
    openai.Embedding.create(model="text-embedding-ada-002", input=input)


client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT, api_key=QDRANT_API_KEY)

client.recreate_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE),
)
