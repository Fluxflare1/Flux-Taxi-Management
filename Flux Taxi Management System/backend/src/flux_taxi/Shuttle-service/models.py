# flux_taxi/shuttle_service/models.py

from django.db import models
from django.contrib.auth.models import User

class ShuttleRoute(models.Model):
    route_name = models.CharField(max_length=100)
    stops = models.TextField()  # Comma-separated list of stops
    schedule = models.TextField()  # Comma-separated list of times

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    route = models.ForeignKey(ShuttleRoute, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
