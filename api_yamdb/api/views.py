from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets, permissions, mixins
from rest_framework.filters import SearchFilter

from .filters import TitleFilter
from reviews.models import Title, Category, Genre
from .serializers import TitleSerializer, CategorySerializer, GenreSerializer
from .pagination import TitlePagination
from .mixins import ListCreateDestroyViewSet


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filterset_class = TitleFilter
    pagination_class = None


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


# class CategoryGenreViewSet(ListCreateDestroyViewSet):
#     filter_backends = (SearchFilter,)
#     search_fields = ('name',)
#     lookup_field = 'slug'

