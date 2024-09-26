# flux_taxi/views.py
import logging

logger = logging.getLogger(__name__)

def some_view(request):
    logger.info("This is an info message")
    # View logic
from django.core.cache import cache

def trip_report(request):
    # Cache key
    cache_key = 'trip_report_stats'
    stats = cache.get(cache_key)

    if not stats:
        total_trips = Trip.objects.count()
        completed_trips = Trip.objects.filter(status='completed').count()
        # Additional calculations...
        
        stats = {
            'total_trips': total_trips,
            'completed_trips': completed_trips,
            # Other stats...
        }
        cache.set(cache_key, stats, timeout=60*15)  # Cache for 15 minutes

    return render(request, 'trip_report.html', stats)
# backend/src/flux_taxi/views.py
def calculate_fare(request):
    distance = request.GET.get('distance')
    time = request.GET.get('time')
    
    base_fare = 50
    cost_per_km = 10
    cost_per_minute = 5
    
    total_fare = base_fare + (cost_per_km * float(distance)) + (cost_per_minute * float(time))
    return JsonResponse({'total_fare': total_fare})
# backend/src/flux_taxi/views.py
from channels.generic.websocket import WebsocketConsumer
import json

class LocationConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
    
    def receive(self, text_data):
        data = json.loads(text_data)
        # Broadcast driver location to passenger
        self.send(text_data=json.dumps({'lat': data['lat'], 'lng': data['lng']}))
# backend/src/flux_taxi/views.py
from rest_framework.views import APIView
from rest_framework.response import Response

class SubmitRating(APIView):
    def post(self, request):
        ride_id = request.data.get('ride_id')
        rating = request.data.get('rating')
        user_type = request.data.get('user_type')  # passenger or driver
        
        ride = Ride.objects.get(id=ride_id)
        if user_type == 'passenger':
            ride.rating_by_passenger = rating
        elif user_type == 'driver':
            ride.rating_by_driver = rating
        ride.save()
        return Response({'status': 'Rating submitted successfully'})
from django.shortcuts import render
from .models import Ride, FareSplit

def fare_splitting_view(request, ride_id):
    ride = Ride.objects.get(id=ride_id)
    if request.method == "POST":
        total_passengers = int(request.POST.get("total_passengers", 1))
        ride.total_passengers = total_passengers
        ride.save()

        for i in range(total_passengers):
            user_id = request.POST.get(f"user_{i}")
            amount_paid = ride.split_fare()
            FareSplit.objects.create(ride=ride, passenger_id=user_id, amount_paid=amount_paid)

        return render(request, 'fare_splitting/success.html', {'ride': ride})

    return render(request, 'fare_splitting/form.html', {'ride': ride})
