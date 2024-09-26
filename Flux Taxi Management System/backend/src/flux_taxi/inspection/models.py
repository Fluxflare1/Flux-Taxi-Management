# flux_taxi/inspection/models.py

from django.db import models
from django.contrib.auth.models import User

class InspectionCenter(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

class Vehicle(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=20)
    inspection_status = models.BooleanField(default=False)

class Inspection(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    inspector = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.BooleanField()  # True for pass, False for fail
