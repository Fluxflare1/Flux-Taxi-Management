from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import RideSharing, RideSharingParticipant
from django.contrib.gis.geos import Point

@api_view(['POST'])
def create_ride_sharing(request):
    pickup_lat = request.data['pickup_lat']
    pickup_lng = request.data['pickup_lng']
    destination_lat = request.data['destination_lat']
    destination_lng = request.data['destination_lng']
    pickup_location = Point(float(pickup_lat), float(pickup_lng))
    destination_location = Point(float(destination_lat), float(destination_lng))

    ride_sharing = RideSharing.objects.create(
        creator=request.user,
        pickup_location=pickup_location,
        destination_location=destination_location
    )
    RideSharingParticipant.objects.create(user=request.user, ride_sharing=ride_sharing)
    return Response({'status': 'Ride sharing created', 'ride_id': ride_sharing.id})

@api_view(['POST'])
def join_ride_sharing(request, ride_id):
    try:
        ride_sharing = RideSharing.objects.get(id=ride_id)
        if ride_sharing.participants.count() < ride_sharing.max_participants:
            RideSharingParticipant.objects.create(user=request.user, ride_sharing=ride_sharing)
            return Response({'status': 'Joined ride sharing'})
        else:
            return Response({'status': 'Ride is full'}, status=400)
    except RideSharing.DoesNotExist:
        return Response({'status': 'Ride not found'}, status=404)
