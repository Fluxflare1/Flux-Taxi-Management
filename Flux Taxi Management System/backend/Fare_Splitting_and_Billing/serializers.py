# fare_splitting_billing/serializers.py

from rest_framework import serializers
from .models import FareSplit

class FareSplitSerializer(serializers.ModelSerializer):
    class Meta:
        model = FareSplit
        fields = '__all__'
