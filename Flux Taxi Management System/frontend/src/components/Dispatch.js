import React, { useState } from 'react';
import axios from 'axios';

function Dispatch() {
    const [pickupLat, setPickupLat] = useState('');
    const [pickupLng, setPickupLng] = useState('');
    const [status, setStatus] = useState('');

    const handleDispatch = (e) => {
        e.preventDefault();
        axios.post('http://localhost:8000/api/auto-dispatch/', {
            pickup_lat: pickupLat,
            pickup_lng: pickupLng,
        })
            .then(response => {
                setStatus(`Driver assigned: ID ${response.data.driver_id}`);
            })
            .catch(error => {
                setStatus('No drivers available');
            });
    };

    return (
        <div>
            <form onSubmit={handleDispatch}>
                <input type="text" value={pickupLat} onChange={(e) => setPickupLat(e.target.value)} placeholder="Pickup Latitude" />
                <input type="text" value={pickupLng} onChange={(e) => setPickupLng(e.target.value)} placeholder="Pickup Longitude" />
                <button type="submit">Dispatch</button>
            </form>
            <p>{status}</p>
        </div>
    );
}

export default Dispatch;
