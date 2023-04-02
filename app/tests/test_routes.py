import io
from fastapi.testclient import TestClient
from requests_toolbelt.multipart.encoder import MultipartEncoder
from fastapi import status
from app import app


client = TestClient(app=app)


def test_entry():
    response = client.get("/")

    assert response.status_code == status.HTTP_200_OK


def upsert_file():
    file_content = open("TheTwitterUserAgreement_1.pdf", "rb")
    file_field = ("TheTwitterUserAgreement_1.pdf", file_content, "application/pdf")

    encoder = MultipartEncoder(fields={"file": file_field})

    response = client.post(
        "/upsert-file",
        headers={"Content-Type": encoder.content_type},
        data=encoder.to_string(),
    )

    return response


def test_upsert_file():
    response = upsert_file()
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"file_name": "TheTwitterUserAgreement_1.pdf"}


def test_chunk_document():
    pass
