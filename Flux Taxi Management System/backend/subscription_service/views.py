# subscription_service/views.py

from rest_framework import viewsets
from .models import SubscriptionPlan, UserSubscription
from .serializers import SubscriptionPlanSerializer, UserSubscriptionSerializer
from rest_framework.response import Response
from django.utils import timezone

class SubscriptionPlanViewSet(viewsets.ModelViewSet):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer

class UserSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer

    def create(self, request, *args, **kwargs):
        plan_id = request.data.get('plan_id')
        plan = SubscriptionPlan.objects.get(id=plan_id)
        end_date = timezone.now() + timezone.timedelta(days=30)  # Assuming monthly plan
        user_subscription = UserSubscription.objects.create(
            user=request.user,
            plan=plan,
            end_date=end_date
        )
        return Response({'message': 'Subscription created successfully', 'subscription_id': user_subscription.id})
