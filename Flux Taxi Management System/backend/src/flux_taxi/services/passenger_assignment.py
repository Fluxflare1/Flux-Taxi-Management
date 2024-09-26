# passenger_assignment.py

from .models import Passenger  # Import your Passenger model

def assign_passenger_to_driver(passenger, driver):
    # Logic to assign the passenger to the driver
    passenger.driver = driver
    passenger.save()  # Save the changes to the database

def assign_passengers_to_driver(driver):
    preferred_dest = driver.preferred_destination
    if preferred_dest:
        passengers = Passenger.objects.filter(destination=preferred_dest)  # Assuming you have a Passenger model
        for passenger in passengers:
            assign_passenger_to_driver(passenger, driver)  # Your function to assign passenger to the driver
