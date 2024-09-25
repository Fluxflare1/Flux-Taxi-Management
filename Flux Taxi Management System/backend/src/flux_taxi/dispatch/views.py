from rest_framework import viewsets
from .models import Dispatcher, RideRequest
from .serializers import DispatcherSerializer, RideRequestSerializer
from rest_framework.permissions import IsAuthenticated

class DispatcherViewSet(viewsets.ModelViewSet):
    queryset = Dispatcher.objects.all()
    serializer_class = DispatcherSerializer
    permission_classes = [IsAuthenticated]

class RideRequestViewSet(viewsets.ModelViewSet):
    queryset = RideRequest.objects.all()
    serializer_class = RideRequestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically assign a dispatcher when creating a ride request
        serializer.save(dispatcher=self.request.user.dispatcher)
