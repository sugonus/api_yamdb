from rest_framework import status, viewsets, permissions, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Avg
from rest_framework.decorators import action
from api.filters import TitleFilter
from rest_framework.filters import SearchFilter
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from .utils import confirmation_generator
from reviews.models import User, Title, Category, Genre, Review
from .mixins import MixinSet
from .serializers import (CommentSerializer,
                          ReviewSerializer,
                          RegistrationSerializer,
                          AuthTokenSerializer,
                          UserSerializer,
                          TitleSerializer,
                          TitleWriteSerializer,
                          CategorySerializer,
                          GenreSerializer)
from .permissions import (IsAdminOrReadOnly,
                          IsAdmin,
                          IsAdminModeratorOwnerOrReadOnly,
                          IsAdminUserOrReadOnly)


class UserRegistrationView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        username = request.data.get('username')
        email = request.data.get('email')

        if serializer.is_valid():
            serializer.save()
            confirmation_generator(username)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        elif (User.objects.filter(username=username).exists()
              and User.objects.get(username=username).email == email):
            confirmation_generator(username)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class AuthTokenView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.data['username']
            confirmation_code = serializer.data['confirmation_code']
            user = get_object_or_404(User, username=username)

            if confirmation_code == user.confirmation_code:
                refresh = RefreshToken.for_user(user)
                return Response(
                    {'token': str(refresh.access_token)},
                    status=status.HTTP_200_OK
                )

            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdmin,)
    lookup_field = 'username'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=username',)

    @action(
        methods=['GET', 'PATCH'],
        detail=False,
        permission_classes=[permissions.IsAuthenticated],
    )
    def me(self, request):
        user = request.user
        if request.method == 'GET':
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save(role=user.role, partial=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all().annotate(
        Avg('reviews__score')
    ).order_by('name')
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ('retrieve', 'list'):
            return TitleSerializer
        return TitleWriteSerializer


class CategoryViewSet(MixinSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = "slug"


class GenreViewSet(MixinSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminModeratorOwnerOrReadOnly]

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAdminModeratorOwnerOrReadOnly,)

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id, title=title_id)
        serializer.save(author=self.request.user, review=review)
