from django.urls import path
from .views import create_ride_sharing, join_ride_sharing

urlpatterns = [
    path('create/', create_ride_sharing, name='create_ride_sharing'),
    path('join/<int:ride_id>/', join_ride_sharing, name='join_ride_sharing'),
]
