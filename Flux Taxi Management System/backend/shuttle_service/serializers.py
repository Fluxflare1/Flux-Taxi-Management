# shuttle_service/serializers.py

from rest_framework import serializers
from .models import ShuttleRoute, ShuttleBooking

class ShuttleRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShuttleRoute
        fields = '__all__'

class ShuttleBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShuttleBooking
        fields = '__all__'
