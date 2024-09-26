from django.urls import path
from . import views

urlpatterns += [
    path('create/', views.create_trip, name='create_trip'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('assign/', views.assign_trip, name='assign_trip'),
]
