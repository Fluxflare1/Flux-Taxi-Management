# flux_taxi/driver_aggregator/views.py

from django.shortcuts import render, redirect
from .models import Driver, Trip
from .forms import DriverRegistrationForm

def register_driver(request):
    if request.method == 'POST':
        form = DriverRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('driver_profile')
    else:
        form = DriverRegistrationForm()
    return render(request, 'driver_registration.html', {'form': form})

def driver_profile(request):
    driver = Driver.objects.get(user=request.user)
    return render(request, 'driver_profile.html', {'driver': driver})

def trip_management(request):
    trips = Trip.objects.filter(driver__user=request.user)
    return render(request, 'trip_management.html', {'trips': trips})
