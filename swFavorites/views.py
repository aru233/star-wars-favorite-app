from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q, BooleanField, Case, OuterRef, Q, Value, When, Prefetch
from django.http import JsonResponse
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, View
from rest_framework import status
from django.core.exceptions import BadRequest

from .models import Planet, Movie, UserPlanet, UserMovie
from .utils import format_planet_response, format_movie_response
from .controller import PlanetController, MovieController, FavoriteController

class PlanetList(ListView):
    def get(self, request):
        try:
            planet_data = PlanetController().getPlanetList(request)
            return JsonResponse(planet_data, safe=False, status=status.HTTP_200_OK)
        except BadRequest:
            return JsonResponse({'error': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)

class MovieList(ListView):
    def get(self, request):
        try:
            movie_data = MovieController().getMovieList(request)
            return JsonResponse(movie_data, safe=False, status=status.HTTP_200_OK)
        except BadRequest:
            return JsonResponse({'error': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)


class ListFavorite(ListView):
    def get(self, request):
        favorite_list = FavoriteController().getFavoriteList(request)
        return JsonResponse(favorite_list, safe=False, status=status.HTTP_200_OK)


@method_decorator(csrf_exempt, name='dispatch')
class MovieAddFavorite(View):
    def post(self, request):
        try:
            MovieController().addFavoriteMovie(request)   
        except Movie.DoesNotExist:
            return JsonResponse({'error!': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return JsonResponse({'error': 'Error while adding favorite'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return JsonResponse({'status': 'success', 'message': 'Favorite updated successfully'}, status=status.HTTP_200_OK)

            
@method_decorator(csrf_exempt, name='dispatch')
class MovieAddCustomTitle(View):
    def post(self, request):
        try:
            MovieController().addCustomMovieTitle(request)
        except Movie.DoesNotExist:
            return JsonResponse({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND) 
        except Exception as ex:
            return JsonResponse({'error': 'Error while adding favorite'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return JsonResponse({'status': 'success', 'message': 'Custom title added successfully'}, status=status.HTTP_200_OK)
        

@method_decorator(csrf_exempt, name='dispatch')
class PlanetAddFavorite(View):
    def post(self, request):
        try:
            PlanetController().addFavoritePlanet(request)
        except Planet.DoesNotExist:
            return JsonResponse({'error': 'Planet not found'}, status=status.HTTP_404_NOT_FOUND) 
        except Exception as ex:
            return JsonResponse({'error': 'Error while adding favorite'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return JsonResponse({'status': 'success', 'message': 'Custom title added successfully'}, status=status.HTTP_200_OK)

            
@method_decorator(csrf_exempt, name='dispatch')
class PlanetAddCustomName(View):
    def post(self, request):
        try:
            PlanetController().addCustomPlanetName(request) 
        except Planet.DoesNotExist:
            return JsonResponse({'error': 'Planet not found'}, status=status.HTTP_404_NOT_FOUND) 
        except Exception as ex:
            return JsonResponse({'error': 'Error while adding favorite'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return JsonResponse({'status': 'success', 'message': 'Custom title added successfully'}, status=status.HTTP_200_OK)