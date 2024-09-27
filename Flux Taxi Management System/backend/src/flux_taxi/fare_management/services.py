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
