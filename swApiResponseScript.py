import requests
import sqlite3

sw_url = "https://swapi.dev/api/"
sw_url_planet = sw_url + "planets"
sw_url_movie = sw_url + "films"

planet_results = []
movie_results = []

# Loop through all the pages of the response from the SWAPI for planets and collect it in a list
while sw_url_planet:
    response = requests.get(sw_url_planet)
    data = response.json()
    planet_results.extend(data['results'])
    sw_url_planet = data['next'] # Getting the URL for the next page

# Loop through all the pages of the response from the SWAPI for planets and collect it in a list
while sw_url_movie:
    response = requests.get(sw_url_movie)
    data = response.json()
    movie_results.extend(data['results'])
    sw_url_movie = data['next'] # Getting the URL for the next page

dbconn = sqlite3.connect('db.sqlite3')

cursor = dbconn.cursor()

# Load data into the database tables
for planet in planet_results:
    cursor.execute('''
        INSERT INTO swFavorites_planet (name, url, created, edited, is_favorite)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        planet['name'],
        planet['url'],
        planet['created'],
        planet['edited'],
        False
    ))

for movie in movie_results:
    cursor.execute('''
        INSERT INTO swFavorites_movie (title, url, release_date, created, edited, is_favorite)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        movie['title'],
        movie['url'],
        movie['release_date'],
        movie['created'],
        movie['edited'],
        False
    ))

dbconn.commit()
dbconn.close()

