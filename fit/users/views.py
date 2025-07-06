from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import MainUser
from .serializers import MainUserSerializer
# Create your views here.

class MainUserViewSet(viewsets.ModelViewSet) :
    queryset= MainUser.objects.all() 
    serializer_class= MainUserSerializer
    filter_backends= [DjangoFilterBackend]
    filterset_fields= ['is_completed']
    

