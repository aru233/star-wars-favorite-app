from django.test.utils import setup_test_environment
from django.test import RequestFactory, TestCase
from django.core.exceptions import BadRequest
from django.urls import reverse
import json

from .models import Planet, Movie, UserPlanet, UserMovie 

import datetime
from rest_framework import status 

from .controller import PlanetController, MovieController, FavoriteController

class StarWarsTests(TestCase):
    def setUp(self):
        self.user = '1'
        self.datetime = datetime.datetime(2023, 4, 7, 13, 42, 37, 670709, tzinfo=datetime.timezone.utc)
        self.date = '2014-12-09'
        self.planet = Planet.objects.create(name='testplanet', url='testurl', created=self.datetime, edited=self.datetime)
        self.planet1 = Planet.objects.create(name='testplanet1', url='testurl1', created=self.datetime, edited=self.datetime)
        self.userPlanet = UserPlanet.objects.create(user=self.user, planet=self.planet1, is_favorite=True, custom_name='customplanet')
        self.movie = Movie.objects.create(title='testmovie', release_date=self.date, url='testurl', created=self.datetime, edited=self.datetime)
        self.movie1 = Movie.objects.create(title='testmovie1', release_date=self.date, url='testurl1', created=self.datetime, edited=self.datetime)
        self.userMovie = UserMovie.objects.create(user=self.user, movie=self.movie1, is_favorite=False, custom_name='custommovie1')
        self.factory = RequestFactory()

    def testGetNoUserProvidedMovie(self):
        request = self.factory.get('/', {'user_id': ""})
        with self.assertRaises(BadRequest) as cm:
            PlanetController().getPlanetList(request)
        self.assertEqual(str(cm.exception), 'User ID is required')

    def testGetPlanetList(self):
        request = self.factory.get('/', {'user_id': self.user})
        response = PlanetController().getPlanetList(request=request)
        self.assertEqual(response['count'], 2)

    def testGetNoUserProvidedProvided(self):
        request = self.factory.get('/', {'user_id': ""})
        with self.assertRaises(BadRequest) as cm:
            MovieController().getMovieList(request)
        self.assertEqual(str(cm.exception), 'User ID is required')

    def testAddFavoriteMovie(self):
        request = self.factory.post('/', data={'user_id': self.user, 'title': 'testmovie1'})
        MovieController().addFavoriteMovie(request)
        self.userMovie.refresh_from_db()
        self.assertEqual(self.userMovie.is_favorite, True)

    def testAddFavoritePlanet(self):
        request = self.factory.post('/', data={'user_id': self.user, 'name': 'testplanet1'})
        PlanetController().addFavoritePlanet(request)
        self.userPlanet.refresh_from_db()
        self.assertEqual(self.userPlanet.is_favorite, True)

    def testAddCustomMovieTitle(self):
        request = self.factory.post('/', data={'user_id': self.user, 'title': 'testmovie1', 'custom_title': 'custommovie1'})
        MovieController().addCustomMovieTitle(request)
        self.userMovie.refresh_from_db()
        self.assertEqual(self.userMovie.custom_name, 'custommovie1')

    def testAddCustomPlanetName(self):
        request = self.factory.post('/', data={'user_id': self.user, 'name': 'testplanet1', 'custom_name': 'customplanet1'})
        PlanetController().addCustomPlanetName(request)
        self.userPlanet.refresh_from_db()
        self.assertEqual(self.userPlanet.custom_name, 'customplanet1')