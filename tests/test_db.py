from sqlalchemy import create_engine

from models import User, table_registry


def teste_create_user():
    engine = create_engine("sqlite:///database.db")
    table_registry.metadata.create_all(engine)
    user = User(username="matheus_teste",
                password="123456",
                email="email@boladao.com")

    assert user.username == "matheus_teste"
