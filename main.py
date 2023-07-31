from fastapi import FastAPI, Body, Path, Query, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.security.http import HTTPAuthorizationCredentials # Importando una clase
from pydantic import BaseModel, Field
from typing import Any, Coroutine, Optional, List
from starlette.requests import Request
from jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer

app = FastAPI() # Creando una instancia de FastAPI, se esta creando una aplicación de nombre "app"

# Modificando información de la documentación
app.title = "Mi aplicación con FastAPI"
app.version = "0.0.1"

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request) :
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="Credenciales no son validas")

class User(BaseModel):
    email: str
    password: str

class Movie(BaseModel): # Las validaciones de Fiel es para los rangos
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15) 
    overview: str = Field(min_length=15, max_length=50) 
    year: int = Field(le=2023) 
    rating: float = Field(ge=1, le=2023) # ge: Mayor igual, le: Menor igual
    category: str = Field(min_length=5, max_length=15) 

    class Config:  # Se creo esta clase para incluir las validaciones para los mensajes por Default
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi pelicula",
                "overview": "Descripción de la pelicula",
                "year": 2023,
                "rating": 10.0,
                "category": "Comedia"
            }
        }

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    },
    {
        'id': 2,
        'title': 'Avatar 2',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2023',
        'rating': 7.8,
        'category': 'Acción'    
    } 
]

@app.get('/', tags  = ['home'])
def message():
    return HTMLResponse('<h1>Hello World!</h1>')

@app.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
    return JSONResponse(status_code=200, content=token)Movie

@app.get('/movies', tags = ['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    return JSONResponse(status_code=200, content=movies)

@app.get('/movies/{id}', tags = ['movies'], status_code=200)
def get_movie(id: int = Path(ge=1, le=2000)): # Filtrar una pelicula por su id
    for item in movies:
        if item["id"] == id:
            return JSONResponse(status_code=200, content=item)
    return JSONResponse(status_code=404, content=[]) 

@app.get('/movies/', tags = ['movies'], status_code=200)
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)):
    data = [item for item in movies if item['category']==category]
    return JSONResponse(status_code=200, content=data) 

@app.post('/movies', tags = ['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    movies.append(movie)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la película"})

@app.put('/movies/{id}', tags = ['movies'], response_model=dict, status_code=200)
def update_movie(id:int, movie: Movie) -> dict:
    for item in movies:
        if item["id"] == id:
            item["title"] = movie.title
            item["overview"] = movie.overview
            item["year"] = movie.year
            item["rating"] = movie.rating
            item["category"] = movie.category
            return JSONResponse(status_code=200, content={"message": "Se ha modificado la película"})
        
@app.delete('/movies/{id}', tags = ['movies'], response_model=dict, status_code=200)
def delete_movie(id:int) -> dict:
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return JSONResponse(status_code=200, content={"message": "Se ha eliminado la película"})

