import React from 'react';

const SOSButton = () => {
    const handleSOS = () => {
        // Call backend SOS API
        fetch('/api/sos', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => alert(data.status));
    };

    return (
        <button onClick={handleSOS} style={{ backgroundColor: 'red', color: 'white' }}>
            SOS
        </button>
    );
};

export default SOSButton;
