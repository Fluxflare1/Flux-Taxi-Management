// frontend/src/components/FareEstimate.js
import React, { useState, useEffect } from 'react';

const FareEstimate = ({ distance, time }) => {
    const [fare, setFare] = useState(0);

    useEffect(() => {
        const fetchFare = async () => {
            const response = await fetch(`/api/calculate-fare/?distance=${distance}&time=${time}`);
            const data = await response.json();
            setFare(data.total_fare);
        };

        fetchFare();
    }, [distance, time]);

    return (
        <div>
            <h3>Estimated Fare: ${fare}</h3>
        </div>
    );
};

export default FareEstimate;
