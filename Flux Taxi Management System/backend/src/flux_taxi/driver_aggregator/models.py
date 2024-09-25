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
