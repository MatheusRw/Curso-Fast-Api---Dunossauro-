from pydantic import BaseModel,EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str  
#herda as propriedades de UserSchema quando passo ele na criação do UserDb
class UserDb(UserSchema):
    id: int

class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr
    