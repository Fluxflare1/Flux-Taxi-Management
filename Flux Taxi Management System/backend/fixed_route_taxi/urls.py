# fixed_route_taxi/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FixedRouteViewSet, FixedRouteBookingViewSet

router = DefaultRouter()
router.register(r'fixed-routes', FixedRouteViewSet)
router.register(r'fixed-route-bookings', FixedRouteBookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
