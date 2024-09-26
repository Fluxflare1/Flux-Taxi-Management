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
