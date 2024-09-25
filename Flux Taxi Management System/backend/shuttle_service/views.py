# shuttle_service/views.py

from rest_framework import viewsets
from .models import ShuttleRoute, ShuttleBooking
from .serializers import ShuttleRouteSerializer, ShuttleBookingSerializer

class ShuttleRouteViewSet(viewsets.ModelViewSet):
    queryset = ShuttleRoute.objects.all()
    serializer_class = ShuttleRouteSerializer

class ShuttleBookingViewSet(viewsets.ModelViewSet):
    queryset = ShuttleBooking.objects.all()
    serializer_class = ShuttleBookingSerializer
