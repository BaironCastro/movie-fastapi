from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
import uvicorn
from bd.database import engine, Base
from routers.movie import routerMovie
from routers.users import Login_user
import os

app = FastAPI(
    title="Aprendiendo FastApi",
    description='Una aApi en los primeros pasos',
    version='0.0.1',
)

app.include_router(routerMovie)
app.include_router(Login_user)

Base.metadata.create_all(bind=engine)

movies = [
    {
        'id': 1,
        'title': "El Señor de los Anillos",
        'overview': "Una historia de un hobbit y su aventura en un mundo de magia y fantasía... ",
        'year': 2001,
        'rating': 9.2,
        'category': "Aventuras"
    }
]

@app.get('/', tags=['Inicio'])
def read_root():
    return HTMLResponse('<h2> Hola mundo! </h2>')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    uvicorn.run("main:app", host='0.0.0.0', port=port)
