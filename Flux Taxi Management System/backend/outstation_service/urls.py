# outstation_service/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OutstationTripViewSet

router = DefaultRouter()
router.register(r'outstation-trips', OutstationTripViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
