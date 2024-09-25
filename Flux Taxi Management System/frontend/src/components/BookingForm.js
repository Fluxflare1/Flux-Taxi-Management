import React, { useState } from 'react';
import axios from 'axios';

function BookingForm() {
    const [pickupLocation, setPickupLocation] = useState('');
    const [dropoffLocation, setDropoffLocation] = useState('');
    const [time, setTime] = useState('');

    const handleBooking = (e) => {
        e.preventDefault();
        axios.post('http://localhost:8000/api/book/', {
            pickupLocation,
            dropoffLocation,
            time
        }).then(response => {
            console.log('Booking successful', response.data);
        }).catch(error => {
            console.log('Error booking', error);
        });
    };

    return (
        <form onSubmit={handleBooking}>
            <input type="text" value={pickupLocation} onChange={(e) => setPickupLocation(e.target.value)} placeholder="Pickup Location" />
            <input type="text" value={dropoffLocation} onChange={(e) => setDropoffLocation(e.target.value)} placeholder="Dropoff Location" />
            <input type="time" value={time} onChange={(e) => setTime(e.target.value)} placeholder="Time" />
            <button type="submit">Book Now</button>
        </form>
    );
}

export default BookingForm;
