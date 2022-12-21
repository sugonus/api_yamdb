from django.shortcuts import get_object_or_404
from django.contrib.auth.tokens import default_token_generator
from reviews.models import User
from django.core.mail import send_mail


def get_confirmation_code_and_send_email(username):
    """Генерация и отправка подтверждения."""
    user = get_object_or_404(User, username=username)
    confirmation_code = default_token_generator.make_token(user)
    user.confirmation_code = confirmation_code
    user.save()
    send_mail(
        'Подтверждение',
        confirmation_code,
        'yamdb@yandex.ru',
        [user.email, ],
        fail_silently=False
    )
