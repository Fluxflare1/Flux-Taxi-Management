from django.db import models

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, db_index=True)  # Index on status
    fare = models.DecimalField(max_digits=10, decimal_places=2)
    # Other fields...
# backend/src/flux_taxi/models.py
class Ride(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    rating_by_passenger = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    rating_by_driver = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)

# Additional logic to handle rating submissions
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
