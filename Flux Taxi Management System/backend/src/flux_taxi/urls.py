from django.urls import include, path

urlpatterns = [
    # Other service URLs...
    path('driver-aggregator/', include('driver_aggregator.urls')),
]
# flux_taxi/urls.py

from django.urls import path, include

urlpatterns = [
    path('fare-management/', include('flux_taxi.fare_management.urls')),
    # other app URLs...
]
# flux_taxi/urls.py
from django.urls import path, include

urlpatterns = [
    path('ride-hailing/', include('flux_taxi.ride_hailing.urls')),
    # other url patterns...
]
# flux_taxi/urls.py

from django.urls import include, path

urlpatterns = [
    # Other URLs
    path('corporate_taxi/', include('corporate_taxi.urls')),
]
from django.urls import path
from .views import fare_splitting_view

urlpatterns = [
    path('fare-splitting/<int:ride_id>/', fare_splitting_view, name='fare_splitting'),
]
# backend/src/flux_taxi/urls.py

from django.urls import path, include

urlpatterns = [
    path('carpooling/', include('carpooling.urls')),
    # other paths...
]
# flux_taxi/urls.py

from django.urls import include

urlpatterns = [
    # other URLs
    path('shuttle/', include('flux_taxi.shuttle_service.urls')),
]
# flux_taxi/urls.py

from django.urls import include

urlpatterns = [
    # other URLs
    path('drivers/', include('flux_taxi.driver_aggregator.urls')),
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
    path('fixed-route-taxi/', include('fixed_route_taxi.urls')),
    path('driver-aggregator/', include('driver_aggregator.urls')),
    path('specialty-vehicles/', include('specialty_vehicles.urls')),
    path('carpooling/', include('carpooling.urls')),
    path('shuttle-service/', include('shuttle_service.urls')),
    path('on-demand-dispatch/', include('on_demand_dispatch.urls')),
    path('subscription-service/', include('subscription_service.urls')),
    path('fare-negotiation/', include('fare_negotiation.urls')),
    path('fare-splitting-billing/', include('fare_splitting_billing.urls')),  # Add this line
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
    path('fixed-route-taxi/', include('fixed_route_taxi.urls')),
    path('driver-aggregator/', include('driver_aggregator.urls')),
    path('specialty-vehicles/', include('specialty_vehicles.urls')),
    path('carpooling/', include('carpooling.urls')),
    path('shuttle-service/', include('shuttle_service.urls')),
    path('on-demand-dispatch/', include('on_demand_dispatch.urls')),
    path('subscription-service/', include('subscription_service.urls')),
    path('fare-negotiation/', include('fare_negotiation.urls')),  # Add this line
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
    path('fixed-route-taxi/', include('fixed_route_taxi.urls')),
    path('driver-aggregator/', include('driver_aggregator.urls')),
    path('specialty-vehicles/', include('specialty_vehicles.urls')),
    path('carpooling/', include('carpooling.urls')),
    path('shuttle-service/', include('shuttle_service.urls')),
    path('on-demand-dispatch/', include('on_demand_dispatch.urls')),
    path('subscription-service/', include('subscription_service.urls')),  # Add this line
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
    path('fixed-route-taxi/', include('fixed_route_taxi.urls')),
    path('driver-aggregator/', include('driver_aggregator.urls')),
    path('specialty-vehicles/', include('specialty_vehicles.urls')),
    path('carpooling/', include('carpooling.urls')),
    path('shuttle-service/', include('shuttle_service.urls')),
    path('on-demand-dispatch/', include('on_demand_dispatch.urls')),  # Add this line
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
    path('fixed-route-taxi/', include('fixed_route_taxi.urls')),
    path('driver-aggregator/', include('driver_aggregator.urls')),
    path('specialty-vehicles/', include('specialty_vehicles.urls')),
    path('carpooling/', include('carpooling.urls')),
    path('shuttle-service/', include('shuttle_service.urls')),  # Add this line
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
    path('fixed-route-taxi/', include('fixed_route_taxi.urls')),
    path('driver-aggregator/', include('driver_aggregator.urls')),
    path('specialty-vehicles/', include('specialty_vehicles.urls')),
    path('carpooling/', include('carpooling.urls')),  # Add this line
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
    path('fixed-route-taxi/', include('fixed_route_taxi.urls')),
    path('driver-aggregator/', include('driver_aggregator.urls')),
    path('specialty-vehicles/', include('specialty_vehicles.urls')),  # Add this line
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
    path('fixed-route-taxi/', include('fixed_route_taxi.urls')),
    path('driver-aggregator/', include('driver_aggregator.urls')),
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
