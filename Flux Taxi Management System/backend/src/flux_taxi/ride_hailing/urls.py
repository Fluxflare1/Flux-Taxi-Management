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
