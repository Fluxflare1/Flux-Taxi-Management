# flux_taxi/ride_hailing/views.py
from django.shortcuts import render, redirect
from .forms import RideRequestForm

def request_ride(request):
    if request.method == 'POST':
        form = RideRequestForm(request.POST)
        if form.is_valid():
            ride_request = form.save(commit=False)
            ride_request.user = request.user
            ride_request.save()
            return redirect('ride_confirmation')
    else:
        form = RideRequestForm()
    return render(request, 'ride_hailing/ride_request.html', {'form': form})

def ride_confirmation(request):
    return render(request, 'ride_hailing/ride_confirmation.html')
from rest_framework import viewsets
from .models import Driver, RideRequest, RideHistory
from .serializers import DriverSerializer, RideRequestSerializer, RideHistorySerializer
from rest_framework.permissions import IsAuthenticated

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [IsAuthenticated]

class RideRequestViewSet(viewsets.ModelViewSet):
    queryset = RideRequest.objects.all()
    serializer_class = RideRequestSerializer
    permission_classes = [IsAuthenticated]

class RideHistoryViewSet(viewsets.ModelViewSet):
    queryset = RideHistory.objects.all()
    serializer_class = RideHistorySerializer
    permission_classes = [IsAuthenticated]
