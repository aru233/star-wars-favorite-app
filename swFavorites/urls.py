from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.ListFavorite.as_view(), name='movie-planet-favorite-list'),
    path('planets/', views.PlanetList.as_view(), name='planet-list'),
    path('movies/', views.MovieList.as_view(), name='movie-list'),
    path('movies/custom-title/', views.MovieAddCustomTitle.as_view(), name='movie-custom-title'),
    path('movies/favorite/', views.MovieAddFavorite.as_view(), name='movie-favorite'),
    path('planets/custom-name/', views.PlanetAddCustomName.as_view(), name='planet-custom-name'),
    path('planets/favorite/', views.PlanetAddFavorite.as_view(), name='planet-favorite')
] 