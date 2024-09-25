from rest_framework import viewsets
from .models import Driver, RideRequest, RideHistory
from .serializers import DriverSerializer, RideRequestSerializer, RideHistorySerializer
from rest_framework.permissions import IsAuthenticated

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [IsAuthenticated]

class RideRequestViewSet(viewsets.ModelViewSet):
    queryset = RideRequest.objects.all()
    serializer_class = RideRequestSerializer
    permission_classes = [IsAuthenticated]

class RideHistoryViewSet(viewsets.ModelViewSet):
    queryset = RideHistory.objects.all()
    serializer_class = RideHistorySerializer
    permission_classes = [IsAuthenticated]
