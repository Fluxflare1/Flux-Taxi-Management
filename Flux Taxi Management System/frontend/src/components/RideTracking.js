import React, { useState, useEffect } from 'react';
import axios from 'axios';

const RideTracking = ({ rideId }) => {
  const [driverLocation, setDriverLocation] = useState("");

  useEffect(() => {
    const fetchDriverLocation = () => {
      axios.get(`/api/rides/${rideId}/`)
        .then(response => {
          setDriverLocation(response.data.driver.location);
        })
        .catch(error => {
          console.error("Error fetching driver location", error);
        });
    };
    
    const interval = setInterval(fetchDriverLocation, 5000); // Update every 5 seconds
    return () => clearInterval(interval);
  }, [rideId]);

  return (
    <div>
      <h2>Track Your Ride</h2>
      <p>Driver's current location: {driverLocation}</p>
    </div>
  );
};

export default RideTracking;
