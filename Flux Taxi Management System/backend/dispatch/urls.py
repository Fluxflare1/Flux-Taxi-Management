from django.urls import path
from .views import auto_dispatch

urlpatterns = [
    path('auto-dispatch/', auto_dispatch, name='auto_dispatch'),
]
