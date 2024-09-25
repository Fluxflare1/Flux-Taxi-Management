# flux_taxi/shuttle_service/views.py

from django.shortcuts import render, redirect
from .models import ShuttleRoute, Booking
from .forms import BookingForm

def manage_routes(request):
    routes = ShuttleRoute.objects.all()
    return render(request, 'shuttle_route_management.html', {'routes': routes})

def book_shuttle(request, route_id):
    route = ShuttleRoute.objects.get(id=route_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.route = route
            booking.save()
            return redirect('user_profile')
    else:
        form = BookingForm()
    return render(request, 'shuttle_booking.html', {'route': route, 'form': form})

def user_profile(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'user_profile.html', {'bookings': bookings})
