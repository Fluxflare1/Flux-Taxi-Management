class DriverAggregatorFareCalculator:
    def __init__(self, distance_km):
        self.distance_km = distance_km

    def calculate_fare(self):
        fare_rate = FareRate.objects.get(service_type='Driver Aggregator')
        total_fare = fare_rate.base_fare + (fare_rate.cost_per_km * self.distance_km)
        return total_fare
