from rest_framework import serializers
from .models import FleetOwner, FleetDriver

class FleetOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FleetOwner
        fields = ['owner', 'company_name', 'contact_info', 'date_joined']

class FleetDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = FleetDriver
        fields = ['fleet_owner', 'driver', 'vehicle', 'earnings', 'is_active']
