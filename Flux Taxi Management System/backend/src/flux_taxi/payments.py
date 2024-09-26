import paystack
from .models import Payment

def initiate_payment(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    payment = Payment.objects.create(
        trip=trip,
        amount=trip.fare,
        status="Pending"
    )
    # Paystack initialization
    paystack_api = paystack.PaystackAPI()
    payment_url = paystack_api.get_payment_url(payment.amount, trip.passenger.email)
    return HttpResponseRedirect(payment_url)
# backend/src/flux_taxi/payments.py
import paystack

def process_payment(amount, user):
    paystack_api = paystack.Paystack(secret_key='your_secret_key')
    response = paystack_api.transaction.initialize(
        amount=amount * 100,
        email=user.email
    )
    return response['authorization_url']
