from models import User


def teste_create_user():
    user = User(username="matheus_teste",
                password="123456",
                email="email@boladao.com")

    assert user.username == "matheus_teste"
