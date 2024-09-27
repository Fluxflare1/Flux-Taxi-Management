# In your fare_management/utils.py or wherever you defined the FareCalculator class
class FareCalculator:
    # Existing methods...

    def calculate_corporate_taxi_fare(self):
        rental_duration = self.kwargs.get('rental_duration')  # Duration in hours
        fare_rate = FareRate.objects.get(service_type='Corporate Taxi Service')

        # Corporate taxi fare logic
        return fare_rate.base_fare + (fare_rate.hourly_rate * rental_duration)
