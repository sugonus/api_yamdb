from django.core.validators import MaxValueValidator, MinValueValidator
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


"""
 Свойство рейтингов к классу Title,
 ставится последним
"""
rating = models.IntegerField(
    verbose_name='Рейтинг',
    null=True,
    default=None
)
pass


class Review(models.Model):
    """
    Модель Отзывы c вставленными ссылками
    на классы Tittle и User,
    рейтинги ввиде чисел в нутри свойств
    """
    title = models.ForeignKey(
        """Title""",
        verbose_name='Произведение',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField(
        verbose_name='Текст',
    )
    author = models.ForeignKey(
        """User""",
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    score = models.PositiveSmallIntegerField(
        verbose_name='Рейтинг',
        validators=[
            MinValueValidator(1, 'Допустимы значения от 1 до 10'),
            MaxValueValidator(10, 'Допустимы значения от 1 до 10')
        ]
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        verbose_name = 'Отзыв'
        ordering = ['pub_date']
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='unique_review'
            ),
        ]


class Comment(models.Model):
    """
    Модель Комментарии c вставленными ссылками
    на классы Review и User
    """
    review = models.ForeignKey(
        Review,
        verbose_name='Отзыв',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField(
        verbose_name='Текст',
    )
    author = models.ForeignKey(
        """User""",
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        verbose_name = 'Комментарий'
        ordering = ['pub_date']
