from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá Mundo!"}


def test_create_user(client):
    # Com a adição do pytest fixture não é mais necessário
    # criar o client dentro de cada teste.
    #
    # Basta passar o client como parâmetro que o pytest
    # cuida de criar e injetar automaticamente.
    response = client.post(
        "/users/",
        json={
            "username": "matheus",
            "password": "123456",
            "email": "teste@teste.com",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "username": "matheus",
        "email": "teste@teste.com",
        "id": 1,
    }
