# flux_taxi/inspection/views.py

from django.shortcuts import render, redirect
from .models import Vehicle, InspectionCenter, Inspection
from .forms import RegistrationForm, InspectionScheduleForm

def register_driver(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_inspection')
    else:
        form = RegistrationForm()
    return render(request, 'driver_registration.html', {'form': form})

def schedule_inspection(request):
    if request.method == 'POST':
        form = InspectionScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inspection_results', vehicle_id=form.cleaned_data['vehicle'].id)
    else:
        form = InspectionScheduleForm()
    return render(request, 'inspection_schedule.html', {'form': form})

def inspection_results(request, vehicle_id):
    inspection = Inspection.objects.filter(vehicle_id=vehicle_id).last()
    return render(request, 'inspection_results.html', {'inspection': inspection})

def admin_inspection_center(request):
    centers = InspectionCenter.objects.all()
    return render(request, 'inspection_center_admin.html', {'centers': centers})
