# corporate_taxi_service/views.py

from rest_framework import viewsets
from .models import CorporateAccount, CorporateTrip
from .serializers import CorporateAccountSerializer, CorporateTripSerializer

class CorporateAccountViewSet(viewsets.ModelViewSet):
    queryset = CorporateAccount.objects.all()
    serializer_class = CorporateAccountSerializer

class CorporateTripViewSet(viewsets.ModelViewSet):
    queryset = CorporateTrip.objects.all()
    serializer_class = CorporateTripSerializer
