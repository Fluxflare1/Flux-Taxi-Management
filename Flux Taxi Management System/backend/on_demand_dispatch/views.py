# on_demand_dispatch/views.py

from rest_framework import viewsets
from .models import RideRequest, Driver
from .serializers import RideRequestSerializer, DriverSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class RideRequestViewSet(viewsets.ModelViewSet):
    queryset = RideRequest.objects.all()
    serializer_class = RideRequestSerializer

    @action(detail=False, methods=['post'])
    def request_ride(self, request):
        ride_request = RideRequest.objects.create(
            user=request.user,
            pickup_location=request.data.get('pickup_location'),
            dropoff_location=request.data.get('dropoff_location')
        )
        return Response({'message': 'Ride requested successfully', 'ride_request_id': ride_request.id})

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    @action(detail=False, methods=['post'])
    def update_location(self, request):
        driver = Driver.objects.get(user=request.user)
        driver.current_location = request.data.get('current_location')
        driver.save()
        return Response({'message': 'Driver location updated'})
