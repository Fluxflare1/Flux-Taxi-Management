import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view

PAYSTACK_SECRET_KEY = 'your_paystack_secret_key'

@api_view(['POST'])
def initiate_payment(request):
    amount = request.data['amount']
    email = request.data['email']
    url = 'https://api.paystack.co/transaction/initialize'
    headers = {
        'Authorization': f'Bearer {PAYSTACK_SECRET_KEY}',
        'Content-Type': 'application/json',
    }
    data = {
        'email': email,
        'amount': int(amount) * 100,  # Paystack expects amount in kobo
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return Response(response.json())
    return Response({'error': 'Payment initiation failed'}, status=400)
