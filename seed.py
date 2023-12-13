actors = [{
  "id": 1,
  "name": "Rosaline Jewiss",
  "birth_date": "5/15/1990",
  "country": "Australia"
}, {
  "id": 2,
  "name": "Karleen Simla",
  "birth_date": "5/3/1981",
  "country": "Portugal"
}, {
  "id": 3,
  "name": "Vaughn D'Agostino",
  "birth_date": "11/8/1996",
  "country": "Netherlands"
}, {
  "id": 4,
  "name": "Eleni Escolme",
  "birth_date": "2/27/2000",
  "country": "Tunisia"
}]

movies = [{
  "id": 1,
  "title": "I Saw Mommy Kissing Santa Claus",
  "release_date": "1/22/2021",
  "category": "Children|Comedy",
  "description": "Aliquam non mauris. Morbi non lectus."
}, {
  "id": 2,
  "title": "La Rabbia",
  "release_date": "11/11/2022",
  "category": "Documentary",
  "description": "Mauris ullamcorper purus sit amet nulla. Quisque arcu libero, rutrum ac, lobortis vel, dapibus at, diam. Nam tristique tortor eu pede."
}, {
  "id": 3,
  "title": "Kelly & Cal",
  "release_date": "3/31/2022",
  "category": "Comedy|Drama",
  "description": "Ut tellus. Nulla ut erat id mauris vulputate elementum."
}, {
  "id": 4,
  "title": "Beyond the Gates of Splendor",
  "release_date": "3/20/2021",
  "category": "Documentary",
  "description": "Quisque id justo sit amet sapien dignissim vestibulum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est."
}]

directors = [{
  "id": 1,
  "name": "Dunn Pugh",
  "birth_date": "12/29/1985",
  "country": "Russia"
}, {
  "id": 2,
  "name": "Demetri Godar",
  "birth_date": "2/21/1978",
  "country": "Indonesia"
}, {
  "id": 3,
  "name": "Rosene MacAirt",
  "birth_date": "11/12/1971",
  "country": "Philippines"
}, {
  "id": 4,
  "name": "Cathee Warby",
  "birth_date": "11/26/1983",
  "country": "China"
}]

from models import Actors, Movies, Directors, session

session.add_all([Actors(**actor) for actor in actors])
session.add_all([Movies(**movie) for movie in movies])
session.add_all([Directors(**director) for director in directors])
session.commit()