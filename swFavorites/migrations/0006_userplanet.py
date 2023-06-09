# Generated by Django 4.2 on 2023-04-06 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('swFavorites', '0005_remove_movie_custom_name_remove_movie_is_favorite_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPlanet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_favorite', models.BooleanField(blank=True, default=False, null=True)),
                ('custom_name', models.CharField(blank=True, max_length=100, null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swFavorites.planet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
