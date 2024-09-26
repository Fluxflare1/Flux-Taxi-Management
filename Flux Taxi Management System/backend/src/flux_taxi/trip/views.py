def view_trip(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    context = {'trip': trip}
    return render(request, 'view_trip.html', context)
from .models import Trip
from django.http import HttpResponseRedirect

def create_trip(request):
    if request.method == 'POST':
        pickup = request.POST.get('pickup')
        dropoff = request.POST.get('dropoff')
        fare = calculate_fare(pickup, dropoff)
        trip = Trip.objects.create(
            pickup_location=pickup,
            dropoff_location=dropoff,
            fare=fare,
            status="Pending"
        )
        return HttpResponseRedirect('/trips/')
    return render(request, 'create_trip.html')
from .models import Trip
from driver.models import Driver

def assign_trip(request):
    available_drivers = Driver.objects.filter(is_available=True)
    if available_drivers.exists():
        # Assign the first available driver
        trip = Trip.objects.create(
            driver=available_drivers.first(),
            pickup_location='Location A',
            dropoff_location='Location B',
            fare=1500.00
        )
        trip.save()
    return HttpResponseRedirect('/admin/dashboard/')
