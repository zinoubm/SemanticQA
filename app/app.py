from fastapi import FastAPI, Body, File, UploadFile
from models.api import (
    UpsertRequest,
    UpsertResponse,
    QueryRequest,
    QueryResponse,
    DeleteRequest,
    DeleteResponse,
)


app = FastAPI()


@app.post("/upsert-file")
async def upsert_file(file: UploadFile = File(...)):
    contents = await file.read()
    print(contents)
    return {"status": "upserted file"}


@app.post("/upsert-batch")
async def upsert_batch():
    return {"status": "upserted batch"}


@app.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest = Body(...)):
    print(request)
    return QueryResponse(result="It's a type of users with all permissions")


@app.delete("/delete")
async def delete():
    return {"status": "deleted"}


@app.on_event("startup")
async def startup():
    print("loading")
