from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubscriptionPlanViewSet, UserSubscriptionViewSet, BillingViewSet

router = DefaultRouter()
router.register('plans', SubscriptionPlanViewSet)
router.register('subscriptions', UserSubscriptionViewSet)
router.register('billing', BillingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
