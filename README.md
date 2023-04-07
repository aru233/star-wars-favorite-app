# Star Wars Favorites App

###### A star wars app, build with Django
    This app let's you view and favorite Star Wars Movies and Planets and set custom Movie title/Planet name

## Features
- Loads list of planets and movies from SWAPI (Star Wars API)
- View planets and movies as list, also indicating if they have been marked as favorite or not
    - Allows searching with a name/title and custom name/title if available
- Allows to set planets and movies as favorites
- Allows to give a custom name for planets and movies
    - Custom name used for searching too for the list and favorite APIs
- Pagination support for planets through URL navigation (previous page as well as next page)
    -  Suport available for movies as well, though the count of movie provided by the SWAPI is small
- View the favorite planets and movies on the home page
    - Custom name shown (if set by user)


## Installation Instructions
Run following commands inside the cloned repository 
```
# Create virtual environment
python -m venv webApp

# Activate the virtual environment
source webApp/bin/activate

# Database setup
python manage.py makemigrations
python manage.py migrate

# Install the required packages from requirements.txt
pip install -r requirements.txt

# Run this python script to load data from Star Wars API into database
python3 swApiResponseScript.py
(There are alternative ways, possibly better, way to do this using Fixtures. For this, we're using this script to pre-load db)

# Run the Django development server
python manage.py runserver

# Open your web browser and go to http://localhost:8000 to view the app.
```

## Tech Stack
- Python/Django
    - Framework used to create the app
- Star Wars API ([SWAPI](https://sw-api-rwjfuiltyq-el.a.run.app/))
    - To fetch star wars data for planets & movies

## App Endpoints

### List favorites
**Endpoint**: `/home`

**Method**: GET

**Query Params**:
Name | Description
--- | --- 
user_id | Id of the user

**Response**:

Name | Description
--- | --- 
favorite_movies | List of the movies marked as favorite by the user 
favorite_planets | List of the planets marked as favorite by the user 

### List Planets

##### Feature
- List of planets with Pagination and favorite indicator
- Allows search with name; custom name, if available, used in search.
- Displays the name, created, updated, URL, and is_favourite fields for each planet
- Pagination navigation available through URLs

**Endpoint**: `/planets`

**Method**: GET

**Query Params**:

Name | Description
--- | --- 
user_id | Id of the user. 
name | Search planets with this name.

**Response**:

Name | Description
--- | --- 
count | Total count of results found. 
num_pages | Total number of pages of results found. 
current_page | Current page number.
next_page | Link to the next page of results.
previous_page | Link to the previous page of results.
results | List of planets.

### Add Favorite Planet

##### Features
- Add a planet as favorite

**Endpoint**: `/planets/favorites/`

**Method**: POST

**Input Data**:

Name | Description
--- | --- 
user_id | Id of the user. 
name | Name of the planet.

**Response**:

Name | Description
--- | --- 
status | success.
message | Favorite updated successfully.

### Add Planet Custom Name

##### Features
- Add a custom name for a planet

**Endpoint**: `/planets/custom-name/`

**Method**: POST

**Input Data**:

Name | Description
--- | --- 
user_id | Id of the user. 
name | Name of the planet.
custom_name | Desired custom name of the planet.

**Response**:

Name | Description
--- | --- 
status | success.
message | Custom Name added successfully.

### List Movies

##### Feature
    - List of movies with Pagination and favorite indicator
    - Allows search with title; custom name, if available, is used in search.
    - Displays the title, release_date, created, updated, URL, and is_favourite fields for each planet
    - Pagination navigation available through URLs

**Endpoint**: `/movies`

**Method**: GET

**Query Params**:

Name | Description
--- | --- 
user_id | Id of the user. 
title | Search movies with this title.

**Response**:

Name | Description
--- | --- 
count | Total count of results found. 
num_pages | Total number of pages of results found. 
current_page | Current page number.
next_page | Link to the next page of results.
previous_page | Link to the previous page of results.
results | List of movies.

### Add Favorite Movie

##### Features
- Add a movie as favorite

**Endpoint**: `/movies/favorites/`

**Method**: POST

**Input Data**:

Name | Description
--- | --- 
user_id | Id of the user. 
title | Title of the movie.

**Response**:

Name | Description
--- | --- 
status | success.
message | Favorite updated successfully.

### Add Movie Custom Name

##### Features
- Add a custom name for a movie

**Endpoint**: `/movies/custom-title/`

**Method**: POST

**Input Data**:

Name | Description
--- | --- 
user_id | Id of the user. 
title | Title of the movie.
custom_title | Desired custom title of the movie.

**Response**:

Name | Description
--- | --- 
status | success.
message | Custom Name added successfully.