from random import choice
from django.shortcuts import get_object_or_404
from reviews.models import User
from django.core.mail import send_mail
import string


def confirmation_generator(username):
    """Генерация и отправка подтверждения."""

    confirmation_code = ''
    for _ in range(15):
        confirmation_code += choice(string.ascii_letters + string.digits)

    user = get_object_or_404(User, username=username)
    user.confirmation_code = confirmation_code
    user.save()
    send_mail(
        'Подтверждение',
        confirmation_code,
        'yamdb@yandex.ru',
        [user.email, ],
        fail_silently=False
    )