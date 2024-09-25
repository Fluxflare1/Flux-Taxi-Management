from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DispatcherViewSet, RideRequestViewSet

router = DefaultRouter()
router.register('dispatchers', DispatcherViewSet)
router.register('ride-requests', RideRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
