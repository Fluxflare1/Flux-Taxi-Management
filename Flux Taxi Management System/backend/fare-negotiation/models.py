# fare_negotiation/models.py

from django.db import models
from django.contrib.auth.models import User
from ride_hailing.models import Ride  # Import Ride model from the Ride-Hailing module

class FareNegotiation(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    rider = models.ForeignKey(User, on_delete=models.CASCADE)
    driver = models.ForeignKey(User, related_name='negotiated_fares', on_delete=models.CASCADE)
    initial_fare = models.DecimalField(max_digits=10, decimal_places=2)
    negotiated_fare = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('declined', 'Declined')], default='pending')

    def __str__(self):
        return f"Negotiation for ride {self.ride.id} between {self.rider.username} and {self.driver.username}"
