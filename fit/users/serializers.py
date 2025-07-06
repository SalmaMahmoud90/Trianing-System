from rest_framework import serializers
from .models import MainUser
class MainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ['id', 'name', 'email', 'phone', 'user_type', 'is_completed', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

