# backend/src/flux_taxi/carpooling/models.py

from django.db import models
from django.contrib.auth.models import User

class Ride(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    seats_available = models.IntegerField()
    fare_per_person = models.DecimalField(max_digits=10, decimal_places=2)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    seats_booked = models.IntegerField()
    fare_paid = models.DecimalField(max_digits=10, decimal_places=2)
