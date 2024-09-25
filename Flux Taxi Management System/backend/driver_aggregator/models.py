# driver_aggregator/models.py

from django.db import models
from django.contrib.auth.models import User

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vehicle_details = models.CharField(max_length=255)
    license_number = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.vehicle_details}"

class RideRequest(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    request_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')  # pending, accepted, completed, cancelled

    def __str__(self):
        return f"Ride Request by {self.driver.user.username} at {self.request_time}"
