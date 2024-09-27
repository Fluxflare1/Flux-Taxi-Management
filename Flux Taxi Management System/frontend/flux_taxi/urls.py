# taxi/urls.py
from django.urls import path
from .views import unified_dashboard

urlpatterns = [
    path('dashboard/', unified_dashboard, name='unified_dashboard'),
    # Add other service URLs here...
]
