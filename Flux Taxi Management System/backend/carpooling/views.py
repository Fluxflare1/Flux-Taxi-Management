# carpooling/views.py

from rest_framework import viewsets
from .models import CarpoolRide, CarpoolBooking
from .serializers import CarpoolRideSerializer, CarpoolBookingSerializer

class CarpoolRideViewSet(viewsets.ModelViewSet):
    queryset = CarpoolRide.objects.all()
    serializer_class = CarpoolRideSerializer

class CarpoolBookingViewSet(viewsets.ModelViewSet):
    queryset = CarpoolBooking.objects.all()
    serializer_class = CarpoolBookingSerializer
