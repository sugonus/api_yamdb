from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import (UserRegistrationView,
                    AuthTokenView,
                    UserViewSet,
                    TitleViewSet,
                    CategoryViewSet,
                    GenreViewSet)

app_name = 'api'

router = DefaultRouter()

router.register('users', UserViewSet, basename='users')
router.register('titles', TitleViewSet, basename='titles')
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', UserRegistrationView.as_view(), name='signup'),
    path('v1/auth/token/', AuthTokenView.as_view(), name='auth'),
]
