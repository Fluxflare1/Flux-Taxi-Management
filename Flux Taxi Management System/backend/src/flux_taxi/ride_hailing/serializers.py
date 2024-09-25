from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

class RideRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    fare = models.DecimalField(max_digits=10, decimal_places=2)
    requested_at = models.DateTimeField(default=now)
    status = models.CharField(max_length=50, default="Pending")  # Pending, Accepted, Completed, Cancelled

    def __str__(self):
        return f"{self.user.username} - {self.pickup_location} to {self.dropoff_location}"

class RideHistory(models.Model):
    ride = models.OneToOneField(RideRequest, on_delete=models.CASCADE)
    driver_rating = models.IntegerField(null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.ride.user.username}'s ride history"
