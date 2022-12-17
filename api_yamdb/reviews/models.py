from django.db import models
from django.contrib.auth.models import AbstractUser

from .validators import validate_year


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    ROLES = (
        (USER, 'Пользователь'),
        (MODERATOR, 'Модератор'),
        (ADMIN, 'Администратор')
    )

    bio = models.TextField(
        'Биография',
        blank=True
    )

    role = models.CharField(
        'Роль',
        max_length=10,
        choices=ROLES,
        default=USER
    )

    email = models.CharField(
        'Email',
        max_length=254,
        unique=True
    )

    confirmation_code = models.CharField(
        'Код',
        max_length=15,
        blank=True,
        null=True
    )

    @property
    def is_user(self):
        return self.role == 'user'

    @property
    def is_admin(self):
        return self.is_superuser or self.role == "admin" or self.is_staff

    @property
    def is_moder(self):
        return self.role == 'moderator'


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
        verbose_name='Жанры',
        blank=True
    )
    year = models.IntegerField(
        verbose_name='Год выхода',
        validators=(validate_year,)
    )

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE,
                                 db_column='genre_id')
    title_id = models.ForeignKey(Title, on_delete=models.CASCADE,
                                 db_column='title_id')

    def __str__(self):
        return f'{self.title_id} {self.genre_id}'
