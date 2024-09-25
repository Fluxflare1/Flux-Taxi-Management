# flux_taxi/corporate_taxi/urls.py

from django.urls import path
from .views import corporate_dashboard

urlpatterns = [
    path('dashboard/', corporate_dashboard, name='corporate_dashboard'),
]
