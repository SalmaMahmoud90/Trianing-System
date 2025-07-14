from rest_framework import serializers
from .models import MainUser, Trainee, Course
class MainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ['id', 'name', 'email', 'phone', 'user_type', 'is_completed', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class Trainee_CoursesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name')
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Trainee
        fields = ['id', 'name', 'courses']
