from django.shortcuts import render
from .models import Ride, FareSplit

def fare_splitting_view(request, ride_id):
    ride = Ride.objects.get(id=ride_id)
    if request.method == "POST":
        total_passengers = int(request.POST.get("total_passengers", 1))
        ride.total_passengers = total_passengers
        ride.save()

        for i in range(total_passengers):
            user_id = request.POST.get(f"user_{i}")
            amount_paid = ride.split_fare()
            FareSplit.objects.create(ride=ride, passenger_id=user_id, amount_paid=amount_paid)

        return render(request, 'fare_splitting/success.html', {'ride': ride})

    return render(request, 'fare_splitting/form.html', {'ride': ride})
