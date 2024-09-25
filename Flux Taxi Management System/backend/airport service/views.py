# airport_service/views.py

from rest_framework import viewsets
from .models import AirportTransfer
from .serializers import AirportTransferSerializer

class AirportTransferViewSet(viewsets.ModelViewSet):
    queryset = AirportTransfer.objects.all()
    serializer_class = AirportTransferSerializer
