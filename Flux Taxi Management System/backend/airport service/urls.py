# airport_service/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AirportTransferViewSet

router = DefaultRouter()
router.register(r'airport-transfers', AirportTransferViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
