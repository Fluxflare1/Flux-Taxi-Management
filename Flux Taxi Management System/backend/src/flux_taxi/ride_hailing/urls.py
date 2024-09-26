# flux_taxi/ride_hailing/urls.py
from django.urls import path
from .views import request_ride, ride_confirmation

urlpatterns = [
    path('request/', request_ride, name='request_ride'),
    path('confirmation/', ride_confirmation, name='ride_confirmation'),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DriverViewSet, RideRequestViewSet, RideHistoryViewSet

router = DefaultRouter()
router.register('drivers', DriverViewSet)
router.register('rides', RideRequestViewSet)
router.register('history', RideHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
