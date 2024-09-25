# project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ride-hailing/', include('ride_hailing.urls')),
    path('car-rental/', include('car_rental.urls')),
]
# project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ride-hailing/', include('ride_hailing.urls')),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('authentication.urls')),
]
