// frontend/src/components/Payment.js
import React, { useState } from 'react';

const Payment = ({ amount }) => {
    const [paymentUrl, setPaymentUrl] = useState('');

    const initiatePayment = async () => {
        const response = await fetch('/api/process-payment/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ amount })
        });
        const data = await response.json();
        setPaymentUrl(data.authorization_url);
    };

    return (
        <div>
            <button onClick={initiatePayment}>Pay ${amount}</button>
            {paymentUrl && <a href={paymentUrl}>Complete Payment</a>}
        </div>
    );
};

export default Payment;
