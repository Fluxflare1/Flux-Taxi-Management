# fixed_route_taxi/serializers.py

from rest_framework import serializers
from .models import FixedRoute, FixedRouteBooking

class FixedRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedRoute
        fields = '__all__'

class FixedRouteBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedRouteBooking
        fields = '__all__'
