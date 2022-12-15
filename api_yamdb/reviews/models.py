from django.db import models
from django.contrib.auth import get_user_model

from .validators import validate_year

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        verbose_name='Категория',
        null=True,
    )
    genres = models.ManyToManyField(
        Genre,
        through='GenreTitle',
        related_name='titles',
        # verbose_name='Жанры',
        # blank=True
    )
    year = models.IntegerField(
        verbose_name='Год выхода',
        validators=(validate_year,)
    )

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} {self.genre}'
