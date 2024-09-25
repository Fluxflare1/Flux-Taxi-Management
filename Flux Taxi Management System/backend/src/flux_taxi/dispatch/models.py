from django.db import models
from django.contrib.auth.models import User
from flux_taxi.aggregator.models import FleetDriver

class Dispatcher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class RideRequest(models.Model):
    customer_name = models.CharField(max_length=100)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    requested_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')  # Pending, Assigned, Completed

    assigned_driver = models.ForeignKey(FleetDriver, null=True, blank=True, on_delete=models.SET_NULL)
    dispatcher = models.ForeignKey(Dispatcher, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Ride for {self.customer_name} from {self.pickup_location} to {self.dropoff_location}"
