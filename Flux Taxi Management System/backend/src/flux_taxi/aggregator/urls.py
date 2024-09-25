from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FleetOwnerViewSet, FleetDriverViewSet

router = DefaultRouter()
router.register('fleet-owners', FleetOwnerViewSet)
router.register('fleet-drivers', FleetDriverViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
