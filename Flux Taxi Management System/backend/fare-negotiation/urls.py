# fare_negotiation/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FareNegotiationViewSet

router = DefaultRouter()
router.register(r'negotiations', FareNegotiationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
