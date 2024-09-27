# views.py
from django.shortcuts import render
from .fare_calculator import FareCalculator

def estimate_driver_aggregator_fare(request):
    if request.method == 'POST':
        distance_km = float(request.POST.get('distance_km'))
        fare_calculator = FareCalculator(service_type='Driver Aggregator', distance_km=distance_km)

        estimated_fare = fare_calculator.calculate_fare()
        return render(request, 'fare_management/estimate_fare.html', {'estimated_fare': estimated_fare})

    return render(request, 'fare_management/estimate_fare.html')
from django.shortcuts import render
from .fare_calculator import DriverAggregatorFareCalculator

def estimate_fare(request):
    estimated_fare = None
    if request.method == 'POST':
        distance_km = float(request.POST.get('distance_km'))
        fare_calculator = DriverAggregatorFareCalculator(distance_km)
        estimated_fare = fare_calculator.calculate_fare()

    return render(request, 'driver_aggregator/estimate_fare.html', {'estimated_fare': estimated_fare})
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
