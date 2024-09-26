// frontend/src/components/RatingForm.js
import React, { useState } from 'react';

const RatingForm = ({ rideId, userType }) => {
    const [rating, setRating] = useState(0);
    
    const submitRating = async () => {
        const response = await fetch('/api/submit-rating/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ ride_id: rideId, rating, user_type: userType })
        });
        const data = await response.json();
        console.log(data);
    };

    return (
        <div>
            <h3>Rate Your {userType === 'passenger' ? 'Driver' : 'Passenger'}</h3>
            <input type="number" value={rating} onChange={(e) => setRating(e.target.value)} />
            <button onClick={submitRating}>Submit Rating</button>
        </div>
    );
};

export default RatingForm;
