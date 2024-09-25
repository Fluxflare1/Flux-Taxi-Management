# fare_splitting_billing/models.py

from django.db import models
from django.contrib.auth.models import User
from ride_hailing.models import Ride  # Import Ride model from the Ride-Hailing module

class FareSplit(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    payer = models.ForeignKey(User, related_name='payments', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('paid', 'Paid'), ('pending', 'Pending')], default='pending')

    def __str__(self):
        return f"{self.payer.username} split for ride {self.ride.id} - Amount: {self.amount}"
