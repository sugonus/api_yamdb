from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from reviews.models import  Review


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = 
    permission_classes =

   


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = 
    permission_classes = 

    
