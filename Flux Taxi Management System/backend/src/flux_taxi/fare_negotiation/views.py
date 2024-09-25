from rest_framework import viewsets
from .models import FareNegotiation
from .serializers import FareNegotiationSerializer

class FareNegotiationViewSet(viewsets.ModelViewSet):
    queryset = FareNegotiation.objects.all()
    serializer_class = FareNegotiationSerializer

    def perform_create(self, serializer):
        serializer.save()
