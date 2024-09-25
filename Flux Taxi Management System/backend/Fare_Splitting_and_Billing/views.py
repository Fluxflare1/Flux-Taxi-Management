# fare_splitting_billing/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import FareSplit
from .serializers import FareSplitSerializer

class FareSplitViewSet(viewsets.ModelViewSet):
    queryset = FareSplit.objects.all()
    serializer_class = FareSplitSerializer

    def create(self, request, *args, **kwargs):
        ride_id = request.data.get('ride_id')
        payer_id = request.data.get('payer_id')
        amount = request.data.get('amount')

        fare_split = FareSplit.objects.create(
            ride_id=ride_id,
            payer_id=payer_id,
            amount=amount
        )
        return Response({'message': 'Fare split created', 'split_id': fare_split.id}, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = request.data.get('status')  # Update the status to 'paid' or 'pending'
        instance.save()
        return Response({'message': 'Fare split updated'}, status=status.HTTP_200_OK)
