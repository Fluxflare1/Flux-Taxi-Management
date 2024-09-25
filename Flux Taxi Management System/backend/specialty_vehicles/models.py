# specialty_vehicles/models.py

from django.db import models

class SpecialtyVehicle(models.Model):
    vehicle_type = models.CharField(max_length=100)  # e.g., Luxury, Van, Accessible
    description = models.TextField()
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.vehicle_type

class VehicleBooking(models.Model):
    vehicle = models.ForeignKey(SpecialtyVehicle, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, default='pending')  # pending, confirmed, cancelled

    def __str__(self):
        return f"Booking for {self.vehicle.vehicle_type} by {self.user.username}"
