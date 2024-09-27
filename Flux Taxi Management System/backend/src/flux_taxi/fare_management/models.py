from django.db import models

class FareRate(models.Model):
    service_type = models.CharField(max_length=50)  # e.g., Ride-Hailing, Car Rental, Corporate Taxi, etc.
    base_fare = models.DecimalField(max_digits=10, decimal_places=2)
    cost_per_km = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cost_per_minute = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    flat_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    surcharge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.service_type
# flux_taxi/fare_management/models.py

from django.db import models

class FareRate(models.Model):
    service_type = models.CharField(max_length=50)  # e.g., Ride-Hailing, Car Rental, Shuttle Service
    base_fare = models.DecimalField(max_digits=10, decimal_places=2)
    cost_per_km = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # For distance-based services
    cost_per_minute = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # For time-based services
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # For car rentals
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # For car rentals
    flat_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # For fixed-rate services
    surcharge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.service_type} - Base Fare: {self.base_fare}"
# flux_taxi/fare_management/models.py
from django.db import models

class FareRate(models.Model):
    service_type = models.CharField(max_length=50)  # e.g., Ride-Hailing, Airport Service, Car Rental
    base_fare = models.DecimalField(max_digits=10, decimal_places=2)  # Flat base fare
    cost_per_km = models.DecimalField(max_digits=10, decimal_places=2)  # Cost per kilometer
    cost_per_minute = models.DecimalField(max_digits=10, decimal_places=2)  # Cost per minute of the ride
    surcharge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Additional surcharge
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Discount for promotions or loyalty

    def __str__(self):
        return f"{self.service_type} - Base: {self.base_fare}"

class TripFare(models.Model):
    ride_request = models.OneToOneField('ride_hailing.RideRequest', on_delete=models.CASCADE, related_name='fare')
    distance_km = models.DecimalField(max_digits=10, decimal_places=2)  # Distance in kilometers
    duration_minutes = models.DecimalField(max_digits=10, decimal_places=2)  # Duration of the ride in minutes
    total_fare = models.DecimalField(max_digits=10, decimal_places=2)  # Final fare for the trip

    def __str__(self):
        return f"Fare for {self.ride_request}"
