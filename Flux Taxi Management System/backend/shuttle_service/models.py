# shuttle_service/models.py

from django.db import models

class ShuttleRoute(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    schedule = models.CharField(max_length=200)  # e.g., "Mon-Fri: 8AM, 5PM"
    seats_available = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}: {self.origin} to {self.destination}"

class ShuttleBooking(models.Model):
    shuttle_route = models.ForeignKey(ShuttleRoute, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    seats_booked = models.PositiveIntegerField()
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.user.username} for {self.shuttle_route.name}"
