from django.core.paginator import Paginator
from django.urls import reverse
from django.http import JsonResponse
from django.core.exceptions import BadRequest
from rest_framework import status
from .repo import PlanetRepo, MovieRepo, FavoriteRepo

class PlanetController:
    def getPlanetList(self, request):
        name = request.GET.get('name', '') # get the title query parameter, default to empty string if not provided
        user_id = request.GET.get('user_id')

        if not user_id:
            raise BadRequest('User ID is required')

        planet_data = PlanetRepo().getPlanetList(user_id, name)

        # Paginating the response
        paginator = Paginator(planet_data, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        data = {
            'count': paginator.count,
            'num_pages': paginator.num_pages,
            'current_page': page_obj.number,
            'next_page': self.getPageUrl(page_obj.next_page_number(), user_id) if page_obj.has_next() else None,
            'previous_page': self.getPageUrl(page_obj.previous_page_number(), user_id) if page_obj.has_previous() else None,
            'results': page_obj.object_list
        }

        return data
    
    # Helper function to get URL for Page Navigation
    def getPageUrl(self, page_number, user_id):
        return reverse('planet-list') + f'?user_id={user_id}&page={page_number}'

    def addFavoritePlanet(self, request):
        user_id = request.POST.get('user_id')
        name = request.POST.get('name')
        PlanetRepo().addFavoritePlanet(user_id, name)

    def addCustomPlanetName(self, request):
        user_id = request.POST.get('user_id')
        name = request.POST.get('name')
        custom_name = request.POST.get('custom_name')
        PlanetRepo().addCustomPlanet(user_id, name, custom_name)

class MovieController:
    def getMovieList(self, request):
        title = request.GET.get('title', '') # get the title query parameter, default to empty string if not provided
        user_id = request.GET.get('user_id')

        if not user_id:
            raise BadRequest('User ID is required')

        movie_data = MovieRepo().getMovieList(title, user_id)
        
        # Paginating the response
        paginator = Paginator(movie_data, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        data = {
            'count': paginator.count,
            'num_pages': paginator.num_pages,
            'current_page': page_obj.number,
            'next_page': self.getPageUrl(page_obj.next_page_number(), user_id) if page_obj.has_next() else None,
            'previous_page': self.getPageUrl(page_obj.previous_page_number(), user_id) if page_obj.has_previous() else None,
            'results': page_obj.object_list
        }

        return data

     # Helper function to get URL for Page Navigation
    def getPageUrl(self, page_number, user_id):
        return reverse('movie-list') + f'?user_id={user_id}&page={page_number}'

    def addFavoriteMovie(self, request):
        user_id = request.POST.get('user_id')
        title = request.POST.get('title')
        MovieRepo().addFavoriteMovie(user_id, title)
        
    def addCustomMovieTitle(self, request):
        user_id = request.POST.get('user_id')
        title = request.POST.get('title')
        custom_title = request.POST.get('custom_title')
        MovieRepo().addCustomMovieTitle(user_id, title, custom_title)

class FavoriteController:
    def getFavoriteList(self, request):
        user_id = request.GET.get('user_id')
        return FavoriteRepo().getFavoriteList(user_id)


