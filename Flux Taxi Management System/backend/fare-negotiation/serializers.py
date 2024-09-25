# fare_negotiation/serializers.py

from rest_framework import serializers
from .models import FareNegotiation

class FareNegotiationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FareNegotiation
        fields = '__all__'
