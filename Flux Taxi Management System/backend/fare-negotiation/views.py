# fare_negotiation/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import FareNegotiation
from .serializers import FareNegotiationSerializer

class FareNegotiationViewSet(viewsets.ModelViewSet):
    queryset = FareNegotiation.objects.all()
    serializer_class = FareNegotiationSerializer

    def create(self, request, *args, **kwargs):
        ride_id = request.data.get('ride_id')
        initial_fare = request.data.get('initial_fare')
        rider = request.user

        # Assuming driver is identified by some means (e.g., during ride request)
        driver_id = request.data.get('driver_id')  # Should be passed in the request

        fare_negotiation = FareNegotiation.objects.create(
            ride_id=ride_id,
            rider=rider,
            driver_id=driver_id,
            initial_fare=initial_fare
        )
        return Response({'message': 'Negotiation created', 'negotiation_id': fare_negotiation.id}, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        negotiated_fare = request.data.get('negotiated_fare')
        instance.negotiated_fare = negotiated_fare
        instance.status = 'accepted'  # Or 'declined' based on the business logic
        instance.save()
        return Response({'message': 'Negotiation updated'}, status=status.HTTP_200_OK)
