# on_demand_dispatch/models.py

from django.db import models
from shuttle_service.models import ShuttleRoute  # Importing ShuttleRoute if needed

class Driver(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    current_location = models.CharField(max_length=100)  # e.g., "Latitude, Longitude"
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

class RideRequest(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=100)
    dropoff_location = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='pending')  # e.g., 'pending', 'accepted', 'completed'
    requested_time = models.DateTimeField(auto_now_add=True)
    driver = models.ForeignKey(Driver, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Ride Request by {self.user.username} from {self.pickup_location} to {self.dropoff_location}"
