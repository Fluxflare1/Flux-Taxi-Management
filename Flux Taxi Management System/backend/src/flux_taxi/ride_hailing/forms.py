# flux_taxi/ride_hailing/forms.py
from django import forms
from .models import RideRequest

class RideRequestForm(forms.ModelForm):
    class Meta:
        model = RideRequest
        fields = ['pickup_location', 'dropoff_location']
