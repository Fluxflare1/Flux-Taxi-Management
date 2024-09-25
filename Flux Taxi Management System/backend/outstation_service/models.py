# outstation_service/models.py

from django.db import models
from django.contrib.auth.models import User

class OutstationTrip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    trip_date = models.DateField()
    trip_time = models.TimeField()
    estimated_fare = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='booked')  # booked, completed, cancelled

    def __str__(self):
        return f"Outstation Trip: {self.user.username} from {self.pickup_location} to {self.dropoff_location}"
