from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from .utils import confirmation_generator
from reviews.models import User, Review
from rest_framework.pagination import PageNumberPagination
from .serializers import (CommentSerializer, ReviewSerializer,
                          UserSerializer, RegistrationSerializer, 
                          AuthTokenSerializer, UserSerializer)
from .permissions import IsAdminModeratorOwnerOrReadOnly


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            username = request.data.get('username')
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
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminModeratorOwnerOrReadOnly]

   


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAdminModeratorOwnerOrReadOnly]

    
