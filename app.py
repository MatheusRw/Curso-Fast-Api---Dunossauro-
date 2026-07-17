from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from schemas import Message, UserDb, UserPublic, UserSchema
from sqlalchemy import create_engine,select
from sqlalchemy.orm import Session 
from settings import Settings
from models import User
from database import get_session
app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    session = get_session()
    db_user = session.scalar(
            select(User).where(
                (User.username == user.username) | (User.email == user.email)
            )
        )

    if db_user:
            if db_user.username == user.username:
                raise HTTPException(
                    status_code=HTTPStatus.BAD_REQUEST,
                    detail=f"Username '{user.username}' already registered"
                )
            elif db_user.email == user.email:
                raise HTTPException(
                    status_code=HTTPStatus.BAD_REQUEST,
                    detail=f"Email '{user.email}' already registered"
                )

    db_user = User(
            username=user.username, email=user.email, password=user.password
        )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user