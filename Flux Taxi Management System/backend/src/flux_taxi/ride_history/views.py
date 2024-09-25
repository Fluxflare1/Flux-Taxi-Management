# flux_taxi/ride_history/views.py

from django.shortcuts import render
from .models import RideHistory

def history_view(request):
    user_ride_history = RideHistory.objects.filter(user=request.user)
    return render(request, 'history.html', {'rides': user_ride_history})
