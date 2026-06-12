from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models import User, table_registry


def teste_create_user(session):
    #engine = create_engine("sqlite:///database.db") caso eu querira criar um banco de dados em arquivo, mas como é só para teste, vou usar o banco de dados em memória.
    #table_registry.metadata.create_all(engine)
    #with Session(engine) as session:
        user = User(username="matheus_teste",
                    password="123456",
                    email="email@boladao.com")
        session.add(user)
        session.commit()
        #session.refresh(user)
        result = session.scalar(select(User).where(User.username == "matheus_teste"))

    # assert user.username == "matheus_teste"
    assert user.id == 1
