# carpooling/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarpoolRideViewSet, CarpoolBookingViewSet

router = DefaultRouter()
router.register(r'rides', CarpoolRideViewSet)
router.register(r'bookings', CarpoolBookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
