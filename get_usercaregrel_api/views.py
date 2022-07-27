from rest_framework import viewsets

from .serializers import UserCareLSerializer
from .models import UserCareRel


class UserCareLViewSet(viewsets.ModelViewSet):
    queryset = UserCareRel.objects.all()
    serializer_class = UserCareLSerializer

# Create your views here.
