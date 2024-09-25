from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Driver, Booking
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Distance

@api_view(['POST'])
def auto_dispatch(request):
    pickup_lat = request.data['pickup_lat']
    pickup_lng = request.data['pickup_lng']
    pickup_location = Point(float(pickup_lat), float(pickup_lng))

    # Find the nearest available driver
    available_drivers = Driver.objects.filter(is_available=True).annotate(
        distance=Distance('location', pickup_location)
    ).order_by('distance')[:1]

    if available_drivers.exists():
        driver = available_drivers[0]
        booking = Booking.objects.create(driver=driver, customer=request.user, pickup_location=pickup_location)
        driver.is_available = False  # Mark the driver as busy
        driver.save()
        return Response({'status': 'Driver assigned', 'driver_id': driver.id})
    else:
        return Response({'status': 'No drivers available'}, status=404)
