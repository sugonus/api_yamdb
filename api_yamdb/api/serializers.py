from rest_framework import serializers

from reviews.models import User, Title, Category, Genre


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'bio',
                  'role')


class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)

    class Meta:
        model = User
        fields = ('username', 'email')

    def validate(self, data):
        if data.get('username') != 'me':
            return data
        raise serializers.ValidationError(
            'Выберите другое имя.'
        )


class AuthTokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)

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
            'id', 'name', 'year', 'rating', 'description', 'genres', 'category'
        )

