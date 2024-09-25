# driver_aggregator/views.py

from rest_framework import viewsets
from .models import Driver, RideRequest
from .serializers import DriverSerializer, RideRequestSerializer

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class RideRequestViewSet(viewsets.ModelViewSet):
    queryset = RideRequest.objects.all()
    serializer_class = RideRequestSerializer
