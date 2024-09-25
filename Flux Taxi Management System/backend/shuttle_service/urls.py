# shuttle_service/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShuttleRouteViewSet, ShuttleBookingViewSet

router = DefaultRouter()
router.register(r'routes', ShuttleRouteViewSet)
router.register(r'bookings', ShuttleBookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
