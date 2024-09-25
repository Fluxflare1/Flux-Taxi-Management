from django.db import models
from django.contrib.auth.models import User

class Ride(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fare = models.DecimalField(max_digits=10, decimal_places=2)
    total_passengers = models.IntegerField(default=1)

    def split_fare(self):
        return self.fare / self.total_passengers

class FareSplit(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.passenger.username} - {self.amount_paid}"
