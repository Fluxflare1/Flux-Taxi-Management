# airport_service/serializers.py

from rest_framework import serializers
from .models import AirportTransfer

class AirportTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirportTransfer
        fields = '__all__'
