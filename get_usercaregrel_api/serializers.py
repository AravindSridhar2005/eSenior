# serializers.py

from rest_framework import serializers

from .models import UserCareRel
# Create your models here.

class UserCareLSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCareRel
        fields = ('id', 'user', 'caregiver', 'moneyowed', 'timeworked')