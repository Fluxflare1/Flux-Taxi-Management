# flux_taxi/corporate_taxi/models.py

from django.db import models
from django.contrib.auth.models import User

class CorporateAccount(models.Model):
    company_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    account_manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='account_manager')

    def __str__(self):
        return self.company_name

class CorporateRide(models.Model):
    corporate_account = models.ForeignKey(CorporateAccount, on_delete=models.CASCADE)
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    ride_date = models.DateTimeField(auto_now_add=True)
    fare = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Ride for {self.corporate_account.company_name} on {self.ride_date}"
