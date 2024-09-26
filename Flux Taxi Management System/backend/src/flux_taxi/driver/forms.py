from django import forms
from .models import Driver, Vehicle

class DriverRegistrationForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['license_number', 'vehicle_documents']

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['make', 'model', 'year', 'license_plate']
