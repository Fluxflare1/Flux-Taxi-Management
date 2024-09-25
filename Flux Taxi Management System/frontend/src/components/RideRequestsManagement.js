import React, { useState } from 'react';
import axios from 'axios';

const RideRequestManagement = ({ rideId }) => {
  const [driverId, setDriverId] = useState('');

  const handleInputChange = (event) => {
    setDriverId(event.target.value);
  };

  const assignDriver = () => {
    axios.patch(`/api/ride-requests/${rideId}/`, { assigned_driver: driverId })
      .then(response => {
        console.log("Driver assigned successfully:", response.data);
      })
      .catch(error => {
        console.error("There was an error assigning the driver!", error);
      });
  };

  return (
    <div>
      <h2>Assign Driver</h2>
      <input
        type="text"
        name="driverId"
        value={driverId}
        onChange={handleInputChange}
        placeholder="Driver ID"
      />
      <button onClick={assignDriver}>Assign Driver</button>
    </div>
  );
};

export default RideRequestManagement;
