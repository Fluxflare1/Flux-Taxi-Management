# fare_splitting_billing/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FareSplitViewSet

router = DefaultRouter()
router.register(r'splits', FareSplitViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
