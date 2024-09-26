from django.shortcuts import render, redirect
from .forms import DriverRegistrationForm, VehicleForm
from .models import Driver

def register_driver(request):
    if request.method == 'POST':
        form = DriverRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            driver = form.save(commit=False)
            driver.user = request.user
            driver.save()
            return redirect('driver_dashboard')
    else:
        form = DriverRegistrationForm()
    return render(request, 'driver_register.html', {'form': form})

def driver_dashboard(request):
    driver = Driver.objects.get(user=request.user)
    return render(request, 'driver_dashboard.html', {'driver': driver})
