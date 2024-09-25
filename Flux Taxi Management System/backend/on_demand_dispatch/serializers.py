# on_demand_dispatch/serializers.py

from rest_framework import serializers
from .models import RideRequest, Driver

class RideRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideRequest
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'
