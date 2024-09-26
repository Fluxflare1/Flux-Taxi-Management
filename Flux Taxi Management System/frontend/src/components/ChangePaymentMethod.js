import React, { useState } from 'react';

const ChangePaymentMethod = () => {
    const [method, setMethod] = useState('');

    const handleChangeMethod = () => {
        fetch('/api/change_payment_method', {
            method: 'POST',
            body: JSON.stringify({ payment_method: method }),
            headers: {
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => alert(data.status));
    };

    return (
        <div>
            <input type="text" placeholder="New Payment Method" onChange={(e) => setMethod(e.target.value)} />
            <button onClick={handleChangeMethod}>Change Payment Method</button>
        </div>
    );
};

export default ChangePaymentMethod;
