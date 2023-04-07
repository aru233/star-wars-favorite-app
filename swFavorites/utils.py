
def format_movie_response(custom_name,is_favorite, movie):
    return {
        'title': custom_name or movie.title,
        'release_date': movie.release_date,
        'created': movie.created,
        'edited': movie.edited,
        'url': movie.url,
        'is_favorite': is_favorite
    }

def format_planet_response(custom_name,is_favorite, planet):
    return {
        'name': custom_name or planet.name,
        'created': planet.created,
        'edited': planet.edited,
        'url': planet.url,
        'is_favorite': is_favorite
    }