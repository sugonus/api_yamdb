from django.db import models
from django.contrib.auth.models import AbstractUser


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
    )

    confirmation_code = models.CharField(
        'Код',
        max_length=15,
        blank=True,
        null=True
    )
   
