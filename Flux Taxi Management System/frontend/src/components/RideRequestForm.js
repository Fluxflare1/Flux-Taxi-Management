import React, { useState } from 'react';
import axios from 'axios';

const RideRequestForm = () => {
  const [pickup, setPickup] = useState("");
  const [dropoff, setDropoff] = useState("");

  const requestRide = () => {
    axios.post('/api/rides/', { pickup_location: pickup, dropoff_location: dropoff })
      .then(response => {
        alert("Ride requested successfully!");
      })
      .catch(error => {
        console.error("Error requesting ride", error);
      });
  };

  return (
    <div>
      <h2>Request a Ride</h2>
      <input 
        type="text" 
        placeholder="Pickup Location" 
        value={pickup} 
        onChange={(e) => setPickup(e.target.value)} 
      />
      <input 
        type="text" 
        placeholder="Dropoff Location" 
        value={dropoff} 
        onChange={(e) => setDropoff(e.target.value)} 
      />
      <button onClick={requestRide}>Request Ride</button>
    </div>
  );
};

export default RideRequestForm;
