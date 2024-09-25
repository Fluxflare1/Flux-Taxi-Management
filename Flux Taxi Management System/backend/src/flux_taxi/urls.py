# project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ride-hailing/', include('ride_hailing.urls')),
    path('car-rental/', include('car_rental.urls')),
    path('outstation-service/', include('outstation_service.urls')),
    path('corporate-taxi/', include('corporate_taxi_service.urls')),
    path('airport-service/', include('airport_service.urls')),
    path('fixed-route-taxi/', include('fixed_route_taxi.urls')),
]
# project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ride-hailing/', include('ride_hailing.urls')),
    path('car-rental/', include('car_rental.urls')),
    path('outstation-service/', include('outstation_service.urls')),
    path('corporate-taxi/', include('corporate_taxi_service.urls')),
    path('airport-service/', include('airport_service.urls')),
]
# project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ride-hailing/', include('ride_hailing.urls')),
    path('car-rental/', include('car_rental.urls')),
    path('outstation-service/', include('outstation_service.urls')),
    path('corporate-taxi/', include('corporate_taxi_service.urls')),
]
# project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ride-hailing/', include('ride_hailing.urls')),
    path('car-rental/', include('car_rental.urls')),
    path('outstation-service/', include('outstation_service.urls')),
    path('corporate-taxi/', include('corporate_taxi_service.urls')),
]
# project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ride-hailing/', include('ride_hailing.urls')),
    path('car-rental/', include('car_rental.urls')),
    path('outstation-service/', include('outstation_service.urls')),
]
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
