from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserRegistrationView, AuthTokenView, UserViewSet

app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register('users', UserViewSet, basename='users')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup/', UserRegistrationView.as_view(), name='signup'),
    path('v1/auth/token/', AuthTokenView.as_view(), name='auth')
]
