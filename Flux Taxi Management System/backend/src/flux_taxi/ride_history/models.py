# flux_taxi/ride_history/models.py

from django.db import models

class RideHistory(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
    ride_date = models.DateTimeField(auto_now_add=True)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    fare = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Ride by {self.user.username} on {self.ride_date}"
