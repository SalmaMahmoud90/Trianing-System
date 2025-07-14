from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import MainUser, Trainee
from .serializers import MainUserSerializer, Trainee_CoursesSerializer
# Create your views here.

class MainUserViewSet(viewsets.ModelViewSet) :
    queryset= MainUser.objects.all() 
    serializer_class= MainUserSerializer
    filter_backends= [DjangoFilterBackend]
    filterset_fields= ['is_completed']
    
class Trainee_CoursesAPIView(APIView) :
    def get(self,request) :
        trainees= Trainee.objects.all()
        trainee_data = Trainee_CoursesSerializer(trainees, many= True).data
        return Response(trainee_data)
