from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    created = models.DateTimeField()
    edited = models.DateTimeField()

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    created = models.DateTimeField()
    edited = models.DateTimeField()
    url = models.URLField()

class UserMovie(models.Model):
    user = models.CharField(max_length=8)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False, blank=True, null=True)
    custom_name = models.CharField(max_length=100, blank=True, null=True)

class UserPlanet(models.Model):
    user = models.CharField(max_length=8)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False, blank=True, null=True)
    custom_name = models.CharField(max_length=100, blank=True, null=True)