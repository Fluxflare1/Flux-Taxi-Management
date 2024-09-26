# flux_taxi/inspection/forms.py

from django import forms
from .models import Vehicle, InspectionCenter

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['registration_number']

class InspectionScheduleForm(forms.ModelForm):
    class Meta:
        model = Inspection
        fields = ['vehicle', 'inspector', 'date']
