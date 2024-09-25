# flux_taxi/shuttle_service/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('manage-routes/', views.manage_routes, name='manage_routes'),
    path('book/<int:route_id>/', views.book_shuttle, name='book_shuttle'),
    path('profile/', views.user_profile, name='user_profile'),
]
