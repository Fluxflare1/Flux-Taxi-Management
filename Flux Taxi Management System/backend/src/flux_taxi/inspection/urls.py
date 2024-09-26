# flux_taxi/inspection/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_driver, name='register_driver'),
    path('schedule/', views.schedule_inspection, name='schedule_inspection'),
    path('results/<int:vehicle_id>/', views.inspection_results, name='inspection_results'),
    path('admin/centers/', views.admin_inspection_center, name='admin_inspection_center'),
]
