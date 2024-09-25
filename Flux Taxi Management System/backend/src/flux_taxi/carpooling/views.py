# backend/src/flux_taxi/carpooling/views.py

from django.shortcuts import render, redirect
from .models import Ride, Booking
from .forms import RideForm

def create_ride(request):
    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ride_listing')
    else:
        form = RideForm()
    return render(request, 'carpooling/ride_creation.html', {'form': form})

def ride_listing(request):
    rides = Ride.objects.all()
    return render(request, 'carpooling/ride_listing.html', {'rides': rides})
