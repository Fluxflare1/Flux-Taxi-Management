import React, { useState } from 'react';

const BookForSomeone = () => {
    const [passengerInfo, setPassengerInfo] = useState({ name: '', contact: '' });

    const handleBookForSomeone = () => {
        fetch('/api/book_ride_for_someone', {
            method: 'POST',
            body: JSON.stringify(passengerInfo),
            headers: {
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => alert(data.status));
    };

    return (
        <div>
            <input type="text" placeholder="Name" onChange={(e) => setPassengerInfo({...passengerInfo, name: e.target.value})} />
            <input type="text" placeholder="Contact" onChange={(e) => setPassengerInfo({...passengerInfo, contact: e.target.value})} />
            <button onClick={handleBookForSomeone}>Book Ride for Someone</button>
        </div>
    );
};

export default BookForSomeone;
