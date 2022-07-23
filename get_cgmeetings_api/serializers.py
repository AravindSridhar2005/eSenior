# serializers.py

from rest_framework import serializers

from .models import Meetings

class CgMeetingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meetings
        fields = ('id', 'senior', 'caregiver', 'timestamp', 'notes', 'recording')