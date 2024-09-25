import React, { useState, useEffect } from 'react';
import axios from 'axios';

const DispatcherDashboard = () => {
  const [rideRequests, setRideRequests] = useState([]);

  useEffect(() => {
    // Fetch ride requests from the API
    axios.get('/api/ride-requests/')
      .then(response => {
        setRideRequests(response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the ride requests!", error);
      });
  }, []);

  return (
    <div>
      <h2>Dispatcher Dashboard</h2>
      <ul>
        {rideRequests.map(ride => (
          <li key={ride.id}>
            {ride.customer_name}: {ride.pickup_location} to {ride.dropoff_location}
            <button>Assign Driver</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default DispatcherDashboard;
