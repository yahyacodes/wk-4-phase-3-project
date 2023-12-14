from fastapi import FastAPI
from models import session, Actors, Movies, Directors
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Movies pydantic BaseModel
class MoviesModel(BaseModel):
    id :int
    title :str
    description :str
    release_date :str
    director_id :int
    category :str

# Actors pydantic BaseModel
class ActorsModel(BaseModel):
    id :int
    name :str
    country :str
    birth_date :str

# Actors pydantic BaseModel
class DirectorsModel(BaseModel):
    id :int
    name :str
    country :str
    birth_date :str

# Fetching Actors on loading
@app.get('/actors')
def get_actors():
    actors = session.query(Actors).all()
    return actors

# Fetching songle Actor
@app.get('/actors/{id}')
def single_actor(id:int) -> ActorsModel:
    single_actor = session.query(Actors).filter_by(id=id).first()
    return single_actor

# Updating actors
@app.patch('/actors/{id}')
def update_actor(id:int, data:ActorsModel):
    actor = session.query(Actors).filter_by(id=id).first()
    for key, value in data.dict(exclude_unset=True).items():
        setattr(actor, key, value)
    session.commit()
    return {'Actor updated successfully'}

# Fetching directors on loading
@app.get('/directors')
def get_directors():
    directors = session.query(Directors).all()
    return directors

# Fetching single director
@app.get('/directors/{id}')
def single_director(id:int) -> DirectorsModel:
    single_director = session.query(Directors).filter_by(id=id).first()
    return single_director

# Updating directors
@app.patch('/directors/{id}')
def update_director(id:int, data:DirectorsModel):
    director = session.query(Directors).filter_by(id=id).first()
    for key, value in data.dict(exclude_unset=True).items():
        setattr(director, key, value)
    session.commit()
    return {'Director updated successfully'}

# Fetching movies on loading
@app.get('/movies')
def get_movies() -> List[MoviesModel]:
    movies = session.query(Movies).all()
    return movies

# Fetching single movie
@app.get('/movies/{id}')
def single_movie(id:int) -> MoviesModel:
    single_movie = session.query(Movies).filter_by(id=id).first()
    return single_movie

# Adding new movie
@app.post('/movies')
def add_new_movie(data:MoviesModel)-> MoviesModel:
    new_movie = Movies(**data.dict())
    session.add(new_movie)
    session.commit()
    return new_movie

# Updating movies
@app.patch('/movies/{id}')
def update_movie(id:int, data:MoviesModel):
    movie = session.query(Movies).filter_by(id=id).first()
    for key, value in data.dict(exclude_unset=True).items():
        setattr(movie, key, value)
    session.commit()
    return {'Movie updated successfully'}

# Deleting movies
@app.delete('/movies/{id}')
def delete_movie(id:int):
    movie = session.query(Movies).filter_by(id=id).first()
    session.delete(movie)
    session.commit()
    return {'One movie has been deleted successfully'}