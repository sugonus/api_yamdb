from django.core.exceptions import ValidationError
from re import match


def validate_username(value):
    if value != 'me' and match(r'[\w]', value):
        return value
    raise ValidationError('Некорректный username')
