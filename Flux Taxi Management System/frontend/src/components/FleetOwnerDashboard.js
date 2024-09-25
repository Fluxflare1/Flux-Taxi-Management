import React, { useState, useEffect } from 'react';
import axios from 'axios';

const FleetOwnerDashboard = () => {
  const [drivers, setDrivers] = useState([]);

  useEffect(() => {
    // Fetch drivers from the API
    axios.get('/api/fleet-drivers/')
      .then(response => {
        setDrivers(response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the drivers!", error);
      });
  }, []);

  return (
    <div>
      <h2>Fleet Owner Dashboard</h2>
      <ul>
        {drivers.map(driver => (
          <li key={driver.id}>{driver.driver.username} - {driver.vehicle}</li>
        ))}
      </ul>
    </div>
  );
};

export default FleetOwnerDashboard;
