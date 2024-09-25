python manage.py makemigrations
python manage.py migrate
from django.contrib.gis.db import models
from django.contrib.auth.models import User

class RideSharing(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_rides')
    pickup_location = models.PointField()
    destination_location = models.PointField()
    max_participants = models.IntegerField(default=4)
    timestamp = models.DateTimeField(auto_now_add=True)

class RideSharingParticipant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ride_sharing = models.ForeignKey(RideSharing, on_delete=models.CASCADE, related_name='participants')
