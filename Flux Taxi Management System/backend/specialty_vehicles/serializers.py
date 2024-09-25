# specialty_vehicles/serializers.py

from rest_framework import serializers
from .models import SpecialtyVehicle, VehicleBooking

class SpecialtyVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialtyVehicle
        fields = '__all__'

class VehicleBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleBooking
        fields = '__all__'
