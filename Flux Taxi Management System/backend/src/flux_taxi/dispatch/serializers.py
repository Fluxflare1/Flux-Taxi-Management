from rest_framework import serializers
from .models import Dispatcher, RideRequest

class DispatcherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispatcher
        fields = ['user', 'name', 'contact_number']

class RideRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideRequest
        fields = ['customer_name', 'pickup_location', 'dropoff_location', 'requested_time', 'status', 'assigned_driver', 'dispatcher']
