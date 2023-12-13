from fastapi import FastAPI
from models import session, Actors, Movies, Directors
from pydantic import BaseModel
from typing import List

app = FastAPI()

class MoviesModel(BaseModel):
    id :int
    title :str
    description :str
    release_date :str
    director_id :int
    category :str

@app.get('/')
def home():
    return {'data': 'Hello'}

@app.get('/actors')
def get_actors():
    actors = session.query(Actors).all()
    return actors

@app.get('/directors')
def get_directors():
    directors = session.query(Directors).all()
    return directors

@app.get('/movies')
def get_movies() -> List[MoviesModel]:
    movies = session.query(Movies).all()
    return movies

@app.get('/movies/{id}')
def single_movie(id:int) -> MoviesModel:
    single_movie = session.query(Movies).filter_by(id=id).first()
    return single_movie

@app.delete('/movies/{id}')
def delete_movie(id:int):
    movie = session.query(Movies).filter_by(id=id).first()
    session.delete(movie)
    session.commit()
    return {'One movie has been deleted successfully'}

@app.post('/movies')
def add_new_movie(data:MoviesModel)-> MoviesModel:
    new_movie = Movies(**data.dict())
    session.add(new_movie)
    session.commit()
    return new_movie

@app.patch('/movies/{id}')
def update_movie(id:int, data:MoviesModel):
    movie = session.query(Movies).filter_by(id=id).first()
    for key, value in data.dict(exclude_unset=True).items():
        setattr(movie, key, value)
    session.commit()
    return {'Movie updated successfully'}