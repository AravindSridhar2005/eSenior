# serializers.py

from rest_framework import serializers
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'last_name', 'email', 'first_name')