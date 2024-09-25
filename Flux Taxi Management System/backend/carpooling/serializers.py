# carpooling/serializers.py

from rest_framework import serializers
from .models import CarpoolRide, CarpoolBooking

class CarpoolRideSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarpoolRide
        fields = '__all__'

class CarpoolBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarpoolBooking
        fields = '__all__'
