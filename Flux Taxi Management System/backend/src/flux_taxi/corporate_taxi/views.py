# flux_taxi/corporate_taxi/views.py

from django.shortcuts import render
from .models import CorporateRide, CorporateAccount

def corporate_dashboard(request):
    corporate_rides = CorporateRide.objects.filter(corporate_account__account_manager=request.user)
    return render(request, 'corporate_taxi.html', {'corporate_rides': corporate_rides})
