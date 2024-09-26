# flux_taxi/flux_taxi/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inspection/', include('inspection.urls')),  # Add this line
]
