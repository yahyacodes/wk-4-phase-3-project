from sqlalchemy import Integer, Column, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, backref

Base = declarative_base()

class Actors(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    birth_date = Column(Integer)
    country = Column(String)
    movies = relationship("Movies", back_populates="actor")

class Movies(Base):
    __tablename__ = 'movies'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    release_date = Column(Integer)
    category = Column(String)
    director_id = Column(Integer, ForeignKey('directors.id'))
    director = relationship("Directors", back_populates="movies")
    actor = relationship("Actors", back_populates="movies")

class Directors(Base):
    __tablename__ = 'directors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    birth_date = Column(Integer)
    country = Column(String)
    movies = relationship("Movies", back_populates="director")


enigne = create_engine('sqlite:///movies.db')
Session = sessionmaker(bind=enigne)
session = Session()
Base.metadata.create_all(bind=enigne)