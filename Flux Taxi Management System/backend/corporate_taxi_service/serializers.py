# corporate_taxi_service/serializers.py

from rest_framework import serializers
from .models import CorporateAccount, CorporateTrip

class CorporateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorporateAccount
        fields = '__all__'

class CorporateTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorporateTrip
        fields = '__all__'
