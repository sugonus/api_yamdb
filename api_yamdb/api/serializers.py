from rest_framework import serializers

from reviews.models import Title, Category, Genre


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
    # category = serializers.SlugRelatedField(
    #     slug_field='slug', queryset=Category.objects.all()
    # )

    class Meta:
        model = Title
        fields = ('id', 'category', 'genres', 'name', 'year', 'description')
