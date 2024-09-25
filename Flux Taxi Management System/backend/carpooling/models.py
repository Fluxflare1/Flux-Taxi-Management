# carpooling/models.py

from django.db import models

class CarpoolRide(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    available_seats = models.PositiveIntegerField()
    driver = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # User model for driver
    status = models.CharField(max_length=20, default='active')  # active, completed, canceled

    def __str__(self):
        return f"{self.origin} to {self.destination} by {self.driver.username}"

class CarpoolBooking(models.Model):
    carpool_ride = models.ForeignKey(CarpoolRide, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    seats_booked = models.PositiveIntegerField()
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.user.username} for {self.carpool_ride}"
