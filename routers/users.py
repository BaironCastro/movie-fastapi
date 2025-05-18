from fastapi import APIRouter
from fastapi.responses import JSONResponse, HTMLResponse
from pydantic import BaseModel
from user_jwt import createToken

Login_user = APIRouter()

class User(BaseModel):
    email: str
    password: str
    
@Login_user.post('/login', tags=['authenticaction'])
def login(user: User):
    if user.email == 'admin@admin.com' and user.password == 'admin':
        token: str = createToken(user.dict())
        print(token)
        return JSONResponse(content=token)   