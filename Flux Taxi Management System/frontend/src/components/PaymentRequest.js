import React, { useState } from 'react';

const PaymentRequest = () => {
    const [contact, setContact] = useState('');

    const handleRequestPayment = () => {
        fetch('/api/request_payment', {
            method: 'POST',
            body: JSON.stringify({ contact }),
            headers: {
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => alert(data.status));
    };

    return (
        <div>
            <input type="text" placeholder="Family/Friend Contact" onChange={(e) => setContact(e.target.value)} />
            <button onClick={handleRequestPayment}>Request Payment</button>
        </div>
    );
};

export default PaymentRequest;
