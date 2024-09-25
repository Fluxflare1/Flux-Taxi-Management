# corporate_taxi_service/models.py

from django.db import models
from django.contrib.auth.models import User

class CorporateAccount(models.Model):
    company_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return self.company_name

class CorporateTrip(models.Model):
    corporate_account = models.ForeignKey(CorporateAccount, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=255)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    trip_date = models.DateField()
    trip_time = models.TimeField()
    estimated_fare = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='booked')  # booked, completed, cancelled

    def __str__(self):
        return f"{self.employee_name}'s trip from {self.pickup_location} to {self.dropoff_location}"
