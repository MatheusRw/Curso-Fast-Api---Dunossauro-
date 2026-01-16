from fastapi import FastAPI
from http import HTTPStatus 
from schemas import Message,UserSchema,UserPublic,UserDb

app = FastAPI()

database = []

@app.get('/',status_code=HTTPStatus.OK,response_model=Message)

def read_root():
    return {'message': 'Olá Mundo!'}


@app.post('/users/',status_code=HTTPStatus.CREATED,response_model=UserPublic)
def create_user(user: UserSchema):

    user_with_id = UserDb(id=len(database)+1,**user.model_dump())


    return user_with_id  
