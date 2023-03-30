import os
from qdrant_client import QdrantClient
from qdrant_client.http import models
from dotenv import load_dotenv
import openai
from uuid import uuid4
from typing import List


load_dotenv()

COLLECTION_NAME = os.getenv("COLLECTION_NAME")
COLLECTION_SIZE = os.getenv("COLLECTION_SIZE")
QDRANT_PORT = os.getenv("QDRANT_PORT")
QDRANT_HOST = os.getenv("QDRANT_HOST")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY


def get_embedding(prompt, model="text-embedding-ada-002"):
    prompt = prompt.replace("\n", " ")

    embedding = None
    try:
        embedding = openai.Embedding.create(input=[prompt], model=model)["data"][0][
            "embedding"
        ]

    except Exception as err:
        print(f"Sorry, There was a problem {err}")

    return embedding


def get_embeddings(prompts: List[str], model="text-embedding-ada-002"):
    prompts = [prompt.replace("\n", " ") for prompt in prompts]

    embeddings = None
    try:
        embeddings = openai.Embedding.create(input=prompts, model=model)["data"]

    except Exception as err:
        print(f"Sorry, There was a problem {err}")

    return [embedding["embedding"] for embedding in embeddings]


def init_qdrant(recreate: bool = False):
    client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT, api_key=QDRANT_API_KEY)

    if recreate:
        client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=models.VectorParams(
                size=COLLECTION_SIZE, distance=models.Distance.COSINE
            ),
        )

    return client


def display_collection_info(collection_info):
    print("Points count:")
    print(collection_info.points_count)
    print("Vectors count:")
    print(collection_info.vectors_count)
    print("Indexed vectors count:")
    print(collection_info.indexed_vectors_count)


def upsert_point(id, payload, embedding, collection_name, client):
    response = client.upsert(
        collection_name=collection_name,
        points=[
            models.PointStruct(
                id=id,
                payload=payload,
                vector=embedding,
            ),
        ],
    )

    return response


def upsert_points(ids, payloads, embeddings, collection_name, client):
    response = client.upsert(
        collection_name=collection_name,
        points=models.Batch(
            ids=ids,
            payloads=payloads,
            vectors=embeddings,
        ),
    )

    return response


def search_point(query_vector, limit, collection_name, client):
    response = client.search(
        collection_name=collection_name,
        query_vector=query_vector,
        limit=limit,
    )

    return response


def delete_collection(collection_name, client):
    response = client.delete_collection(collection_name=collection_name)

    return response


if __name__ == "__main__":
    client = init_qdrant()

    # getting the collection and displaying info
    collection_info = client.get_collection(collection_name=COLLECTION_NAME)
    display_collection_info(collection_info)

    # upsert a point
    # record_id = uuid4().hex
    # record_payload = {"title": "Dreaming big", "chunk": "wow this is great"}
    # record_embedding = get_embedding(record_payload["chunk"])

    # response = upsert_point(
    #     record_id,
    #     record_payload,
    #     record_embedding,
    #     COLLECTION_NAME,
    #     client,
    # )

    # upsert batch
    # record_ids = [uuid4().hex for x in range(3)]
    # record_payloads = [
    #     {
    #         "title": "War",
    #         "chunk": """
    #             War is an intense armed conflict[a] between states, governments, societies, or paramilitary groups such as mercenaries, insurgents, and militias. It is generally characterized by extreme violence, destruction, and mortality, using regular or irregular military forces. Warfare refers to the common activities and characteristics of types of war, or of wars in general.[2] Total war is warfare that is not restricted to purely legitimate military targets, and can result in massive civilian or other non-combatant suffering and casualties.
    #             While some war studies scholars consider war a universal and ancestral aspect of human nature,[3] others argue it is a result of specific socio-cultural, economic or ecological circumstances.[4]
    #         """,
    #     },
    #     {
    #         "title": "Car",
    #         "chunk": """
    #             A car or automobile is a motor vehicle with wheels. Most definitions of cars say that they run primarily on roads, seat one to eight people, have four wheels, and mainly transport people (rather than goods).
    #      """,
    #     },
    #     {
    #         "title": "Horse",
    #         "chunk": "The horse (Equus ferus caballus)[2][3] is a domesticated, one-toed, hoofed mammal. It belongs to the taxonomic family Equidae and is one of two extant subspecies of Equus ferus. The horse has evolved over the past 45 to 55 million years from a small multi-toed creature, Eohippus, into the large, single-toed animal of today. Humans began domesticating horses around 4000 BCE, and their domestication is believed to have been widespread by 3000 BCE. Horses in the subspecies caballus are domesticated, although some domesticated populations live in the wild as feral horses. These feral populations are not true wild horses, as this term is used to describe horses that have never been domesticated. There is an extensive, specialized vocabulary used to describe equine-related concepts, covering everything from anatomy to life stages, size, colors, markings, breeds, locomotion, and behavior.",
    #     },
    # ]
    # record_embeddings = get_embeddings(
    #     [record_payload["chunk"] for record_payload in record_payloads]
    # )

    # response = upsert_points(
    #     record_ids,
    #     record_payloads,
    #     record_embeddings,
    #     COLLECTION_NAME,
    #     client,
    # )

    # search point
    query_embedding = get_embedding("what is a horse")

    response = search_point(query_embedding, 1, COLLECTION_NAME, client)

    print(response)

    # delete all points
    # res = delete_collection(COLLECTION_NAME, client)
    # print(res)
