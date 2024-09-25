from django.db import models
from django.contrib.auth.models import User

class FleetOwner(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name

class FleetDriver(models.Model):
    fleet_owner = models.ForeignKey(FleetOwner, related_name='drivers', on_delete=models.CASCADE)
    driver = models.OneToOneField(User, on_delete=models.CASCADE)
    vehicle = models.CharField(max_length=100)
    earnings = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.driver.username} ({self.vehicle})"
