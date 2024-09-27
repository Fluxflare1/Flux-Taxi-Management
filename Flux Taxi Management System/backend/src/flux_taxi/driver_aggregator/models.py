from django.db import models

class FareRate(models.Model):
    service_type = models.CharField(max_length=50)  # e.g., Ride-Hailing, Driver Aggregator
    base_fare = models.DecimalField(max_digits=10, decimal_places=2)
    cost_per_km = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cost_per_minute = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    flat_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    surcharge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.service_type} Fare Rate"
# models.py
class FareRate(models.Model):
    service_type = models.CharField(max_length=50)  # e.g., Ride-Hailing, Driver Aggregator
    base_fare = models.DecimalField(max_digits=10, decimal_places=2)
    cost_per_km = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Only for services using distance
    cost_per_minute = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # For time-based services
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # For car rentals
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # For rentals
    flat_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # For fixed routes or airport service
    surcharge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
class FareRate(models.Model):
    service_type = models.CharField(max_length=50)  # e.g., Driver Aggregator
    base_fare = models.DecimalField(max_digits=10, decimal_places=2)
    cost_per_km = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # Other fields can be included as needed...
# flux_taxi/driver_aggregator/models.py

from django.db import models
from django.contrib.auth.models import User

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=15)
    availability = models.BooleanField(default=True)

class Trip(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=100)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    fare = models.DecimalField(max_digits=10, decimal_places=2)
    trip_date = models.DateTimeField(auto_now_add=True)
