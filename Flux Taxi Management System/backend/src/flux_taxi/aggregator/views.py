from rest_framework import viewsets
from .models import FleetOwner, FleetDriver
from .serializers import FleetOwnerSerializer, FleetDriverSerializer
from rest_framework.permissions import IsAuthenticated

class FleetOwnerViewSet(viewsets.ModelViewSet):
    queryset = FleetOwner.objects.all()
    serializer_class = FleetOwnerSerializer
    permission_classes = [IsAuthenticated]

class FleetDriverViewSet(viewsets.ModelViewSet):
    queryset = FleetDriver.objects.all()
    serializer_class = FleetDriverSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return drivers for the authenticated fleet owner
        return FleetDriver.objects.filter(fleet_owner__owner=self.request.user)
