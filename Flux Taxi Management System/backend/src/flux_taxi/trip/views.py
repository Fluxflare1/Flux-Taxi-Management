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
