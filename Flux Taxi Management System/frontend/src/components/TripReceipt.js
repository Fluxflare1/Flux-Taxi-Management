import React, { useEffect, useState } from 'react';

const TripReceipt = ({ tripId }) => {
    const [receipt, setReceipt] = useState(null);

    useEffect(() => {
        fetch(`/api/trip_receipt/${tripId}`)
        .then(response => response.json())
        .then(data => setReceipt(data));
    }, [tripId]);

    return (
        <div>
            {receipt ? <pre>{JSON.stringify(receipt, null, 2)}</pre> : <p>Loading receipt...</p>}
        </div>
    );
};

export default TripReceipt;
