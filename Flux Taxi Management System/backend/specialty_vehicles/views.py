# specialty_vehicles/views.py

from rest_framework import viewsets
from .models import SpecialtyVehicle, VehicleBooking
from .serializers import SpecialtyVehicleSerializer, VehicleBookingSerializer

class SpecialtyVehicleViewSet(viewsets.ModelViewSet):
    queryset = SpecialtyVehicle.objects.all()
    serializer_class = SpecialtyVehicleSerializer

class VehicleBookingViewSet(viewsets.ModelViewSet):
    queryset = VehicleBooking.objects.all()
    serializer_class = VehicleBookingSerializer
