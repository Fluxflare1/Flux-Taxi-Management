from django.shortcuts import render
from .models import Trip

def trip_report(request):
    total_trips = Trip.objects.count()
    completed_trips = Trip.objects.filter(status='completed').count()
    pending_trips = Trip.objects.filter(status='pending').count()
    cancelled_trips = Trip.objects.filter(status='cancelled').count()

    context = {
        'total_trips': total_trips,
        'completed_trips': completed_trips,
        'pending_trips': pending_trips,
        'cancelled_trips': cancelled_trips,
    }
    return render(request, 'trip_report.html', context)
from django.shortcuts import render
from trip.models import Trip

def admin_dashboard(request):
    trips = Trip.objects.all()
    context = {'trips': trips}
    return render(request, 'admin_dashboard.html', context)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from flux_taxi.models import Booking, Driver, Vehicle, Earnings

@login_required
def admin_dashboard(request):
    total_bookings = Booking.objects.count()
    active_drivers = Driver.objects.filter(is_active=True).count()
    available_vehicles = Vehicle.objects.filter(is_available=True).count()
    total_earnings = Earnings.objects.all().aggregate(Sum('amount'))['amount__sum']

    context = {
        'total_bookings': total_bookings,
        'active_drivers': active_drivers,
        'available_vehicles': available_vehicles,
        'total_earnings': total_earnings,
    }

    return render(request, 'admin/dashboard.html', context)
