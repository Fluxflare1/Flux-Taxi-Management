# flux_taxi/driver/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('set_destination/', views.set_preferred_destination, name='set_preferred_destination'),  # New URL
    # Other driver-related URLs
]
urlpatterns += [
    path('toggle_availability/', views.toggle_availability, name='toggle_availability'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_driver, name='register_driver'),
    path('dashboard/', views.driver_dashboard, name='driver_dashboard'),
]
