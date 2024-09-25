from django.contrib.gis.db import models
from django.contrib.auth.models import User

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    location = models.PointField()  # Requires GeoDjango

class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    pickup_location = models.PointField()
    timestamp = models.DateTimeField(auto_now_add=True)
