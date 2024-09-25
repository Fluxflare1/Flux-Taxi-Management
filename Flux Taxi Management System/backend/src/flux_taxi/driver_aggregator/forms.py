# flux_taxi/driver_aggregator/forms.py

from django import forms
from django.contrib.auth.models import User

class DriverRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
