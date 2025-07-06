from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MainUserViewSet


router = DefaultRouter()
router.register(r'users', MainUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

