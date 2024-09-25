# corporate_taxi_service/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CorporateAccountViewSet, CorporateTripViewSet

router = DefaultRouter()
router.register(r'corporate-accounts', CorporateAccountViewSet)
router.register(r'corporate-trips', CorporateTripViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
