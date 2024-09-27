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
