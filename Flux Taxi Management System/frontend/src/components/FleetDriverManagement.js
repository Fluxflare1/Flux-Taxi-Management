import React, { useState } from 'react';
import axios from 'axios';

const FleetDriverManagement = () => {
  const [driver, setDriver] = useState({ vehicle: '', driverId: '' });

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setDriver({ ...driver, [name]: value });
  };

  const addDriver = () => {
    axios.post('/api/fleet-drivers/', driver)
      .then(response => {
        console.log("Driver added successfully:", response.data);
      })
      .catch(error => {
        console.error("There was an error adding the driver!", error);
      });
  };

  return (
    <div>
      <h2>Fleet Driver Management</h2>
      <input
        type="text"
        name="driverId"
        value={driver.driverId}
        onChange={handleInputChange}
        placeholder="Driver ID"
      />
      <input
        type="text"
        name="vehicle"
        value={driver.vehicle}
        onChange={handleInputChange}
        placeholder="Vehicle"
      />
      <button onClick={addDriver}>Add Driver</button>
    </div>
  );
};

export default FleetDriverManagement;
