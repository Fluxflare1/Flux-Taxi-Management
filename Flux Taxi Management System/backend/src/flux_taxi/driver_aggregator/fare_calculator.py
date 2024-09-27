# fare_calculator.py
class FareCalculator:
    def __init__(self, service_type, **kwargs):
        self.service_type = service_type
        self.kwargs = kwargs

    def calculate_fare(self):
        if self.service_type == 'Ride-Hailing':
            return self.calculate_ride_hailing_fare()
        elif self.service_type == 'Car Rental':
            return self.calculate_car_rental_fare()
        elif self.service_type == 'Driver Aggregator':
            return self.calculate_driver_aggregator_fare()
        # Add other services

    # Existing fare calculation methods...

    def calculate_driver_aggregator_fare(self):
        distance_km = self.kwargs.get('distance_km')
        fare_rate = FareRate.objects.get(service_type='Driver Aggregator')

        # Driver aggregator fare logic
        total_fare = fare_rate.base_fare
        total_fare += fare_rate.cost_per_km * distance_km
        return total_fare
class DriverAggregatorFareCalculator:
    def __init__(self, distance_km):
        self.distance_km = distance_km

    def calculate_fare(self):
        fare_rate = FareRate.objects.get(service_type='Driver Aggregator')
        total_fare = fare_rate.base_fare + (fare_rate.cost_per_km * self.distance_km)
        return total_fare
