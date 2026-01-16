from http import HTTPStatus

from fastapi.testclient import TestClient

from app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá Mundo!"}


def test_create_user():
    client = TestClient(app)
    response = client.post(
        "/users/",
        json={
            "username": "matheus",
            "password": "123456",
            "email": "teste@teste.com"
        }
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "username": "matheus",
        "email": "teste@teste.com",
        "id": 1
    }
