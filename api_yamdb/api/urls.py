from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (UserRegistrationView, AuthTokenView, UserViewSet,
                    TitleViewSet,
                    CategoryViewSet,
                    GenreViewSet,
                    CommentViewSet, ReviewViewSet)

app_name = 'api'

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('titles', TitleViewSet, basename='titles')
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet, basename='reviews')
router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)'
                '/comments', CommentViewSet, basename='comments')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', UserRegistrationView.as_view(), name='signup'),
    path('v1/auth/token/', AuthTokenView.as_view(), name='auth'),
]
