from rest_framework import serializers

from .models import CaregiverProfile

class CgMProfileSerializer(serializers.ModelSerializer):
    
    qualifications = serializers.CharField(default="")
    priceperhour = serializers.DecimalField(max_digits=7, decimal_places=2, default="0.00")
    
    class Meta:
        model = CaregiverProfile
        fields = ('user', 'qualifications', 'priceperhour')
        read_only_fields = ['user']