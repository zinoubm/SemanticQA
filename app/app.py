from fastapi import FastAPI, Body, File, UploadFile
from models.api import (
    UpsertResponse,
    QuestionRequest,
    QuestionResponse,
)

from models.models import Question

from parser.parser import get_document_from_file
from documents import upsert_document, delete_datastore
from question_answering import answer_question


app = FastAPI()


@app.get("/")
async def info():
    return {
        "api": "SemanticQA",
        "version": "1",
    }


@app.post("/upsert-file", response_model=UpsertResponse)
async def upsert_file(file: UploadFile = File(...)):
    document = await get_document_from_file(file)
    ids = upsert_document(document)

    return UpsertResponse(ids=ids)


@app.post("/question", response_model=QuestionResponse)
async def question(request: QuestionRequest = Body(...)):

    question = Question(question=request.question)
    answer = answer_question(question)

    return QuestionResponse(answer=answer)


@app.delete("/delete")
async def delete():
    status = delete_datastore()
    return {"status": status}
