# flux_taxi/fare_management/views.py

from django.shortcuts import render
from .services import FareCalculator

def estimate_fare(request):
    if request.method == 'POST':
        service_type = request.POST.get('service_type')

        if service_type == 'Ride-Hailing':
            distance_km = float(request.POST.get('distance_km'))
            duration_minutes = float(request.POST.get('duration_minutes'))
            fare_calculator = FareCalculator(service_type='Ride-Hailing', distance_km=distance_km, duration_minutes=duration_minutes)
        elif service_type == 'Car Rental':
            rental_duration = float(request.POST.get('rental_duration'))
            fare_calculator = FareCalculator(service_type='Car Rental', rental_duration=rental_duration)
        # Add other services

        estimated_fare = fare_calculator.calculate_fare()
        return render(request, 'fare_management/estimate_fare.html', {'estimated_fare': estimated_fare})

    return render(request, 'fare_management/estimate_fare.html')
# flux_taxi/fare_management/views.py

from django.shortcuts import render
from django.http import HttpResponse

# Example fare calculation logic (customize as needed)
def estimate_fare(request):
    estimated_fare = None
    if request.method == 'POST':
        service_type = request.POST.get('service_type')
        distance_km = float(request.POST.get('distance_km'))
        duration_minutes = float(request.POST.get('duration_minutes'))
        
        # Sample fare calculation based on service type (customize this logic)
        if service_type == 'Ride-Hailing':
            base_fare = 100  # Example base fare
            per_km_rate = 50  # Example rate per km
            per_min_rate = 10  # Example rate per minute
        elif service_type == 'Car Rental':
            base_fare = 500  # Example base fare for car rental
            per_km_rate = 20  # Example rate per km for rental
            per_min_rate = 5  # Example rate per minute for rental
        else:
            base_fare = 100  # Default base fare
            per_km_rate = 50  # Default rate per km
            per_min_rate = 10  # Default rate per minute
        
        # Calculate the estimated fare
        estimated_fare = base_fare + (per_km_rate * distance_km) + (per_min_rate * duration_minutes)

    return render(request, 'fare_management/estimate_fare.html', {'estimated_fare': estimated_fare})
# flux_taxi/fare_management/views.py
from django.shortcuts import render, get_object_or_404
from .services import FareCalculator
from .models import TripFare, FareRate
from ride_hailing.models import RideRequest

def estimate_fare(request):
    if request.method == 'POST':
        service_type = request.POST.get('service_type')
        distance_km = float(request.POST.get('distance_km'))
        duration_minutes = float(request.POST.get('duration_minutes'))

        fare_calculator = FareCalculator(service_type, distance_km, duration_minutes)
        estimated_fare = fare_calculator.calculate_fare()

        return render(request, 'fare_management/estimate_fare.html', {
            'estimated_fare': estimated_fare
        })

    return render(request, 'fare_management/estimate_fare.html')

def ride_fare(request, ride_request_id):
    ride_request = get_object_or_404(RideRequest, id=ride_request_id)
    
    fare_calculator = FareCalculator(
        service_type='Ride-Hailing', 
        distance_km=ride_request.distance_km, 
        duration_minutes=ride_request.duration_minutes
    )
    
    total_fare = fare_calculator.calculate_fare()
    
    # Save fare for the trip
    TripFare.objects.create(
        ride_request=ride_request,
        distance_km=ride_request.distance_km,
        duration_minutes=ride_request.duration_minutes,
        total_fare=total_fare
    )
    
    return render(request, 'fare_management/ride_fare.html', {
        'ride_request': ride_request,
        'total_fare': total_fare
    })
