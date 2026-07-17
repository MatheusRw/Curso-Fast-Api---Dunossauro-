from sqlalchemy import select

from models import User


def teste_create_user(session):
    user = User(
        username="testuser",
        email="teste@teste",
        password="123456"
    )
    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.username == "testuser")
    )

    assert result.username == "testuser"
