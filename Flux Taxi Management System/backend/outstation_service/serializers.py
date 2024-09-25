# outstation_service/serializers.py

from rest_framework import serializers
from .models import OutstationTrip

class OutstationTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutstationTrip
        fields = '__all__'
