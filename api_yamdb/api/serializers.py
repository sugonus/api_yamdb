from rest_framework import serializers
from re import match
from reviews.models import User, Title, Category, Genre


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name',
                  'bio',
                  'role')


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')

    def validate_username(self, value):
        if value != 'me' and match(r'[\w]', value):
            return value
        raise serializers.ValidationError('Некорректный username')

    def validate_email(self, value):
        if match(r'[\w]+@[\w]+\.[\w]+', value):
            return value
        raise serializers.ValidationError('Некорректный email')


class AuthTokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    confirmation_code = serializers.CharField(max_length=15)

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')


class GenreSerializer(serializers.ModelSerializer):
    """Жанры, описание."""

    class Meta:
        model = Genre
        fields = ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):
    """Категории, описание."""

    titles = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'titles')


class TitleSerializer(serializers.ModelSerializer):
    """Произведения, описание."""

    genres = GenreSerializer(read_only=True, many=True)
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Title
        fields = ('id', 'category', 'genres', 'name', 'year', 'description')


class ReadOnlyTitleSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(
        source='reviews__score__avg', read_only=True
    )
    genres = GenreSerializer(read_only=True, many=True)
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Title
        fields = (
            'id', 'name', 'year', 'rating', 'description', 'genre', 'category'
        )
