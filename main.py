from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from bd.database import engine, Base
from routers.movie import routerMovie
from routers.users import Login_user

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


