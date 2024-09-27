from django.urls import path
from .views import estimate_fare

urlpatterns = [
    path('estimate-fare/', estimate_fare, name='estimate_fare'),
]
# In driver_aggregator/urls.py
urlpatterns = [
    path('estimate-fare/', estimate_fare, name='driver_aggregator_estimate_fare'),
]
# flux_taxi/driver_aggregator/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_driver, name='register_driver'),
    path('profile/', views.driver_profile, name='driver_profile'),
    path('trips/', views.trip_management, name='trip_management'),
]
