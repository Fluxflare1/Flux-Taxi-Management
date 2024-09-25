# specialty_vehicles/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SpecialtyVehicleViewSet, VehicleBookingViewSet

router = DefaultRouter()
router.register(r'vehicles', SpecialtyVehicleViewSet)
router.register(r'bookings', VehicleBookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
