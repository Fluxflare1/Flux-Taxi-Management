def set_driver_availability(request, driver_id, availability):
    driver = Driver.objects.get(id=driver_id)
    driver.is_available = availability
    driver.save()
    return HttpResponseRedirect('/driver/dashboard/')
from django.http import HttpResponseRedirect

def toggle_availability(request):
    driver = Driver.objects.get(user=request.user)
    if request.method == 'POST':
        driver.is_available = not driver.is_available
        driver.save()
        return HttpResponseRedirect('/driver/dashboard/')
from .models import Trip

def driver_dashboard(request):
    driver = Driver.objects.get(user=request.user)
    vehicles = driver.vehicle_set.all()
    trips = Trip.objects.filter(driver=driver)

    context = {
        'driver': driver,
        'vehicles': vehicles,
        'trips': trips,
        'total_earnings': sum([trip.fare for trip in trips]),
    }
    return render(request, 'driver_dashboard.html', context)
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
