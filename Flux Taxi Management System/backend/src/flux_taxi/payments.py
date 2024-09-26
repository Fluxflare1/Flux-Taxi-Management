# backend/src/flux_taxi/payments.py
import paystack

def process_payment(amount, user):
    paystack_api = paystack.Paystack(secret_key='your_secret_key')
    response = paystack_api.transaction.initialize(
        amount=amount * 100,
        email=user.email
    )
    return response['authorization_url']
