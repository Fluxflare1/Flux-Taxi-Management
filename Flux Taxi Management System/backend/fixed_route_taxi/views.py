# fixed_route_taxi/views.py

from rest_framework import viewsets
from .models import FixedRoute, FixedRouteBooking
from .serializers import FixedRouteSerializer, FixedRouteBookingSerializer

class FixedRouteViewSet(viewsets.ModelViewSet):
    queryset = FixedRoute.objects.all()
    serializer_class = FixedRouteSerializer

class FixedRouteBookingViewSet(viewsets.ModelViewSet):
    queryset = FixedRouteBooking.objects.all()
    serializer_class = FixedRouteBookingSerializer
