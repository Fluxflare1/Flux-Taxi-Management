import React, { useState } from 'react';
import axios from 'axios';

function RideSharing() {
    const [pickupLat, setPickupLat] = useState('');
    const [pickupLng, setPickupLng] = useState('');
    const [destinationLat, setDestinationLat] = useState('');
    const [destinationLng, setDestinationLng] = useState('');
    const [rideId, setRideId] = useState('');
    const [status, setStatus] = useState('');

    const handleCreateRide = (e) => {
        e.preventDefault();
        axios.post('http://localhost:8000/api/ridesharing/create/', {
            pickup_lat: pickupLat,
            pickup_lng: pickupLng,
            destination_lat: destinationLat,
            destination_lng: destinationLng,
        })
            .then(response => {
                setStatus(`Ride created with ID: ${response.data.ride_id}`);
            })
            .catch(error => {
                setStatus('Error creating ride');
            });
    };

    const handleJoinRide = (e) => {
        e.preventDefault();
        axios.post(`http://localhost:8000/api/ridesharing/join/${rideId}/`)
            .then(response => {
                setStatus('Successfully joined the ride');
            })
            .catch(error => {
                setStatus('Error joining ride');
            });
    };

    return (
        <div>
            <h3>Create Ride Sharing</h3>
            <form onSubmit={handleCreateRide}>
                <input type="text" value={pickupLat} onChange={(e) => setPickupLat(e.target.value)} placeholder="Pickup Latitude" />
                <input type="text" value={pickupLng} onChange={(e) => setPickupLng(e.target.value)} placeholder="Pickup Longitude" />
                <input type="text" value={destinationLat} onChange={(e) => setDestinationLat(e.target.value)} placeholder="Destination Latitude" />
                <input type="text" value={destinationLng} onChange={(e) => setDestinationLng(e.target.value)} placeholder="Destination Longitude" />
                <button type="submit">Create Ride</button>
            </form>

            <h3>Join Ride Sharing</h3>
            <form onSubmit={handleJoinRide}>
                <input type="text" value={rideId} onChange={(e) => setRideId(e.target.value)} placeholder="Ride ID" />
                <button type="submit">Join Ride</button>
            </form>
            <p>{status}</p>
        </div>
    );
}

export default RideSharing;
