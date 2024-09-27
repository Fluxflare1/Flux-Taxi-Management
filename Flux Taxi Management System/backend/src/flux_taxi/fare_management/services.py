# flux_taxi/fare_management/services.py

from .models import FareRate

class FareCalculator:
    def __init__(self, service_type, **kwargs):
        self.service_type = service_type
        self.kwargs = kwargs

    def calculate_fare(self):
        if self.service_type == 'Ride-Hailing':
            return self.calculate_ride_hailing_fare()
        elif self.service_type == 'Car Rental':
            return self.calculate_car_rental_fare()
        elif self.service_type == 'Airport Service':
            return self.calculate_airport_fare()
        # Add more service-specific fare calculations here

    def calculate_ride_hailing_fare(self):
        distance_km = self.kwargs.get('distance_km')
        duration_minutes = self.kwargs.get('duration_minutes')
        fare_rate = FareRate.objects.get(service_type='Ride-Hailing')

        total_fare = fare_rate.base_fare
        total_fare += fare_rate.cost_per_km * distance_km
        total_fare += fare_rate.cost_per_minute * duration_minutes
        return total_fare

    def calculate_car_rental_fare(self):
        rental_duration = self.kwargs.get('rental_duration')  # in hours or days
        fare_rate = FareRate.objects.get(service_type='Car Rental')

        if rental_duration < 24:
            return fare_rate.hourly_rate * rental_duration
        else:
            return fare_rate.daily_rate * (rental_duration // 24)

    def calculate_airport_fare(self):
        fare_rate = FareRate.objects.get(service_type='Airport Service')
        return fare_rate.flat_rate

    # Add more calculation methods for other services
# flux_taxi/fare_management/services.py
from .models import FareRate, TripFare

class FareCalculator:
    def __init__(self, service_type, distance_km, duration_minutes):
        self.service_type = service_type
        self.distance_km = distance_km
        self.duration_minutes = duration_minutes

    def calculate_fare(self):
        try:
            # Fetch fare rate for the specific service type
            fare_rate = FareRate.objects.get(service_type=self.service_type)
        except FareRate.DoesNotExist:
            return None

        # Calculate fare based on the rate structure
        total_fare = fare_rate.base_fare
        total_fare += fare_rate.cost_per_km * self.distance_km
        total_fare += fare_rate.cost_per_minute * self.duration_minutes

        # Apply surcharges
        total_fare += fare_rate.surcharge

        # Apply discounts
        total_fare -= fare_rate.discount

        return total_fare
