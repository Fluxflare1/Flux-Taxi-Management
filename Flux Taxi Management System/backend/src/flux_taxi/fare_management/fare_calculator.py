from .models import FareRate  # Adjust import as necessary

class FareCalculator:
    def __init__(self, service_type, **kwargs):
        self.service_type = service_type
        self.kwargs = kwargs

    def calculate_fare(self):
        if self.service_type == 'Ride-Hailing':
            return self.calculate_ride_hailing_fare()
        elif self.service_type == 'Car Rental':
            return self.calculate_car_rental_fare()
        elif self.service_type == 'Corporate Taxi Service':
            return self.calculate_corporate_taxi_fare(self.kwargs.get('distance_km'))
        elif self.service_type == 'Outstation Service':
            return self.calculate_outstation_fare(self.kwargs.get('distance_km'))
        elif self.service_type == 'Carpooling':
            return self.calculate_carpooling_fare(self.kwargs.get('distance_km'), self.kwargs.get('passengers'))
        elif self.service_type == 'Shuttle Service':
            return self.calculate_shuttle_service_fare(self.kwargs.get('route'))
        elif self.service_type == 'Fixed Route Taxi':
            return self.calculate_fixed_route_fare(self.kwargs.get('route'))

    def calculate_corporate_taxi_fare(self, distance):
        fare_rate = FareRate.objects.get(service_type='Corporate Taxi Service')
        total_fare = fare_rate.base_fare + (fare_rate.cost_per_km * distance)
        return total_fare

    def calculate_outstation_fare(self, distance):
        fare_rate = FareRate.objects.get(service_type='Outstation Service')
        return fare_rate.flat_rate  # Modify as needed based on your logic

    def calculate_carpooling_fare(self, distance, passengers):
        fare_rate = FareRate.objects.get(service_type='Carpooling')
        return (fare_rate.base_fare + (fare_rate.cost_per_km * distance)) / passengers

    def calculate_shuttle_service_fare(self, route):
        fare_rate = FareRate.objects.get(service_type='Shuttle Service')
        return fare_rate.flat_rate  # Fixed fare for the route

    def calculate_fixed_route_fare(self, route):
        fare_rate = FareRate.objects.get(service_type='Fixed Route Taxi')
        return fare_rate.flat_rate  # Fixed fare based on the route
