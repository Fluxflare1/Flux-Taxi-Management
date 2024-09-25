from rest_framework import serializers
from .models import SubscriptionPlan, UserSubscription, Billing

class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = ['id', 'name', 'price', 'duration', 'description']

class UserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscription
        fields = ['user', 'plan', 'start_date', 'end_date', 'active']

class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = ['user', 'amount', 'date', 'transaction_id', 'status']
