# on_demand_dispatch/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RideRequestViewSet, DriverViewSet

router = DefaultRouter()
router.register(r'ride-requests', RideRequestViewSet)
router.register(r'drivers', DriverViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
