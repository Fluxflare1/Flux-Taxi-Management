# driver_aggregator/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DriverViewSet, RideRequestViewSet

router = DefaultRouter()
router.register(r'drivers', DriverViewSet)
router.register(r'ride-requests', RideRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
