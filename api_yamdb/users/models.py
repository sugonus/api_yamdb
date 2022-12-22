from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_username


class User(AbstractUser):
    class Role(models.TextChoices):
        USER = "user", "Пользователь"
        MODERATOR = "moderator", "Модератор"
        ADMIN = "admin", "Администратор"

    username = models.CharField(
        'Роль',
        max_length=150,
        unique=True,
        validators=(validate_username,)
    )

    bio = models.TextField(
        'Биография',
        blank=True
    )

    role = models.CharField(
        'Роль',
        max_length=10,
        choices=Role.choices,
        default=Role.USER
    )

    email = models.EmailField(
        'Email',
        max_length=254,
        unique=True
    )

    confirmation_code = models.CharField(
        'Код',
        max_length=50,
        blank=True,
        null=True
    )

    @property
    def is_simple_user(self):
        return self.role == self.Role.USER

    @property
    def is_admin(self):
        return (self.is_superuser
                or self.role == self.Role.ADMIN or self.is_staff)

    @property
    def is_moderator(self):
        return self.role == self.Role.MODERATOR

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('role',)

    def __str__(self):
        return self.username
