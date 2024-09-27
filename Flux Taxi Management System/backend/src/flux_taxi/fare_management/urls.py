# flux_taxi/fare_management/urls.py

from django.urls import path
from .views import estimate_fare

urlpatterns = [
    path('estimate-fare/', estimate_fare, name='estimate_fare'),
]
# flux_taxi/fare_management/urls.py
from django.urls import path
from .views import estimate_fare, ride_fare

urlpatterns = [
    path('estimate/', estimate_fare, name='estimate_fare'),
    path('ride/<int:ride_request_id>/fare/', ride_fare, name='ride_fare'),
]
