from sqlalchemy import Integer, Column, String, create_engine, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

# Many to many relationship between actors and movies
actor_movie_table = Table(
    'actor_movie', 
    Base.metadata,
    Column('actor_id', Integer, ForeignKey('actors.id')),
    Column('movie_id', Integer, ForeignKey('movies.id'))
)

# Creating Actors table
class Actors(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    birth_date = Column(Integer)
    country = Column(String)
    movies = relationship("Movies", secondary=actor_movie_table, back_populates="actor")

# Creating Movies table
class Movies(Base):
    __tablename__ = 'movies'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    release_date = Column(Integer)
    category = Column(String)
    director_id = Column(Integer, ForeignKey('directors.id'))
    director = relationship("Directors", back_populates="movies")
    actor = relationship("Actors", secondary=actor_movie_table, back_populates="movies")

# Creating Directors table
class Directors(Base):
    __tablename__ = 'directors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    birth_date = Column(Integer)
    country = Column(String)
    movies = relationship("Movies", back_populates="director")

# Creating the database
enigne = create_engine('sqlite:///movies.db')
Session = sessionmaker(bind=enigne)
session = Session()
Base.metadata.create_all(bind=enigne)