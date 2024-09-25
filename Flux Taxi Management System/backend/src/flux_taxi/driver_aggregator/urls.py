# flux_taxi/driver_aggregator/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_driver, name='register_driver'),
    path('profile/', views.driver_profile, name='driver_profile'),
    path('trips/', views.trip_management, name='trip_management'),
]
