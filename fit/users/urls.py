from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MainUserViewSet, Trainee_CoursesAPIView


router = DefaultRouter()
router.register(r'users', MainUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('trainees-courses/', Trainee_CoursesAPIView.as_view(), name='trainees-courses'),
]

