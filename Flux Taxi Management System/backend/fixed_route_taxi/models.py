# fixed_route_taxi/models.py

from django.db import models
from django.contrib.auth.models import User

class FixedRoute(models.Model):
    route_name = models.CharField(max_length=255)
    starting_point = models.CharField(max_length=255)
    ending_point = models.CharField(max_length=255)
    fare = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.route_name

class FixedRouteBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    route = models.ForeignKey(FixedRoute, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='booked')  # booked, completed, cancelled

    def __str__(self):
        return f"Booking for {self.route.route_name} by {self.user.username}"
