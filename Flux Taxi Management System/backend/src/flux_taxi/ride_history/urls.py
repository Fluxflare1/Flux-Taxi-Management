# flux_taxi/ride_history/urls.py

from django.urls import path
from .views import history_view

urlpatterns = [
    path('history/', history_view, name='ride_history'),
]
