from .models import Planet, UserPlanet, Movie, UserMovie
from .utils import format_planet_response, format_movie_response

class PlanetRepo:
    def getPlanetList(self, user_id, name):
        planet_data = []
        planets = Planet.objects.all()
        for planet in planets:
            if UserPlanet.objects.filter(user=user_id, planet=planet).exists():
                user_planet = UserPlanet.objects.filter(user=user_id, planet=planet).first()
                is_favorite = user_planet.is_favorite
                custom_name = user_planet.custom_name
            else:
                is_favorite = False
                custom_name = ""

            if name and custom_name != name and planet.name != name: # if name provided in query doesn't match the custom name or name, continue
                continue
            planet_data.append(format_planet_response(custom_name, is_favorite, planet))
            
        return planet_data

    def addFavoritePlanet(self, user_id, name):
        planet = Planet.objects.filter(name=name).first()
        if UserPlanet.objects.filter(planet=planet).exists(): # Updating the entry in UserPlanet table with the custom_name field
            user_planet = UserPlanet.objects.filter(planet=planet).first()
            user_planet.is_favorite = True
            user_planet.save()
        else: # Creating an entry in the UserPlanet table with the custom_name field
            UserPlanet.objects.create(user=user_id, planet=planet, is_favorite=True) 

    def addCustomPlanet(self, user_id, name, custom_name):
        planet = Planet.objects.filter(name=name).first()
        if planet is None:
            raise Planet.DoesNotExist
        if UserPlanet.objects.filter(planet=planet).exists(): # Updating the entry in UserPlanet table with the custom_name field
            user_planet = UserPlanet.objects.filter(planet=planet).first()
            user_planet.custom_name = custom_name
            user_planet.save()
        else: # Creating an entry in the UserPlanet table with the custom_name field
            UserPlanet.objects.create(user=user_id, planet=planet, custom_name=custom_name)

                
class MovieRepo:
    def getMovieList(self, title, user_id):
        movie_data = []

        movies = Movie.objects.all()
        for movie in movies:
            if UserMovie.objects.filter(user=user_id, movie=movie).exists(): # Checking if the movie is a favorite and if it has a custom name
                user_movie = UserMovie.objects.filter(user=user_id, movie=movie).first()
                is_favorite = user_movie.is_favorite
                custom_name = user_movie.custom_name
            else:
                is_favorite = False
                custom_name = ""

            if title and custom_name != title and movie.title != title: # if title provided in query doesn't match the custom name or title, continue
                continue

            movie_data.append(format_movie_response(custom_name, is_favorite, movie))

        return movie_data
    
    def addFavoriteMovie(self, user_id, title):
        movie = Movie.objects.filter(title=title).first()
        if UserMovie.objects.filter(movie=movie).exists(): # Updating the entry in UserMovie table with the custom_name field
            user_movie = UserMovie.objects.filter(movie=movie).first()
            user_movie.is_favorite = True
            user_movie.save()
        else: # Creating an entry in the UserMovie table with the custom_name field
            UserMovie.objects.create(user=user_id, movie=movie, is_favorite=True)

    def addCustomMovieTitle(self, user_id, title, custom_title):
        movie = Movie.objects.filter(title=title).first()
        if movie is None:
            raise Movie.DoesNotExist
        if UserMovie.objects.filter(movie=movie).exists(): # Updating the entry in UserMovie table with the custom_name field
            user_movie = UserMovie.objects.filter(movie=movie).first()
            user_movie.custom_name = custom_title
            user_movie.save()
        else: # Creating an entry in the UserMovie table with the custom_name field
            UserMovie.objects.create(user=user_id, movie=movie, custom_name=custom_title) 


class FavoriteRepo:
    def getFavoriteList(self, user_id):
        favorite_list = []
        favorite_movie_list = []
        favorite_planet_list = []

        user_movies = UserMovie.objects.filter(is_favorite=True)
        user_planets = UserPlanet.objects.filter(is_favorite=True)

        # Get a list of primary keys of the filtered UserMovie rows
        movie_ids = [umovie.movie.id for umovie in user_movies]
        # Get a list of primary keys of the filtered UserPlanet rows
        planet_ids = [uplanet.planet.id for uplanet in user_planets]

        # Filter the Movie table based on the list of primary keys
        favorite_movies = Movie.objects.filter(id__in=movie_ids)
        # Filter the Planet table based on the list of primary keys
        favorite_planets = Planet.objects.filter(id__in=planet_ids)

        for movie in favorite_movies:
            favorite_movie_list.append({
                'title': user_movies.filter(movie=movie).first().custom_name or movie.title
                })

        for planet in favorite_planets:
            favorite_planet_list.append({
                'name': user_planets.filter(planet=planet).first().custom_name or planet.name
                })

        favorite_list.append({
            'favorite_movies': favorite_movie_list,
            'favorite_planets': favorite_planet_list
        })

        return favorite_list
