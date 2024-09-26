from django.urls import path
from .views import trip_report, user_report, earnings_report

urlpatterns = [
    path('trip-report/', trip_report, name='trip_report'),
    path('user-report/', user_report, name='user_report'),
    path('earnings-report/', earnings_report, name='earnings_report'),
]
from django.urls import path
from .views import admin_dashboard

urlpatterns = [
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
]
