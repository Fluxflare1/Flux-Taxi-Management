from django.urls import path
from . import views

urlpatterns += [
    path('initiate/<int:trip_id>/', views.initiate_payment, name='initiate_payment'),
]
