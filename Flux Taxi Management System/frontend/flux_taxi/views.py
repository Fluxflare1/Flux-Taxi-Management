# taxi/views.py
from django.shortcuts import render

def unified_dashboard(request):
    return render(request, 'unified_dashboard.html')
