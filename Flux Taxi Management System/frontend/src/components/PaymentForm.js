import React, { useState } from 'react';
import axios from 'axios';

function PaymentForm() {
    const [amount, setAmount] = useState('');
    const [email, setEmail] = useState('');
    const [paymentUrl, setPaymentUrl] = useState('');

    const handlePayment = (e) => {
        e.preventDefault();
        axios.post('http://localhost:8000/api/payments/initiate/', {
            amount: amount,
            email: email,
        })
            .then(response => {
                setPaymentUrl(response.data.data.authorization_url);
            })
            .catch(error => {
                console.error('Error initiating payment', error);
            });
    };

    return (
        <div>
            <form onSubmit={handlePayment}>
                <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" />
                <input type="text" value={amount} onChange={(e) => setAmount(e.target.value)} placeholder="Amount" />
                <button type="submit">Pay Now</button>
            </form>
            {paymentUrl && <a href={paymentUrl}>Proceed to Paystack</a>}
        </div>
    );
}

export default PaymentForm;
