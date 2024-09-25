# outstation_service/views.py

from rest_framework import viewsets
from .models import OutstationTrip
from .serializers import OutstationTripSerializer

class OutstationTripViewSet(viewsets.ModelViewSet):
    queryset = OutstationTrip.objects.all()
    serializer_class = OutstationTripSerializer
