# backend/src/flux_taxi/carpooling/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_ride, name='create_ride'),
    path('', views.ride_listing, name='ride_listing'),
]
