urlpatterns += [
    path('toggle_availability/', views.toggle_availability, name='toggle_availability'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_driver, name='register_driver'),
    path('dashboard/', views.driver_dashboard, name='driver_dashboard'),
]
