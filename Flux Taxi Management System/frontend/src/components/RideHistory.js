import React, { useState, useEffect } from 'react';
import axios from 'axios';

const RideHistory = () => {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    axios.get('/api/history/')
      .then(response => {
        setHistory(response.data);
      })
      .catch(error => {
        console.error("Error fetching ride history", error);
      });
  }, []);

  return (
    <div>
      <h2>Ride History</h2>
      <ul>
        {history.map(ride => (
          <li key={ride.id}>
            {ride.ride.pickup_location} to {ride.ride.dropoff_location} - {ride.completed_at}
          </li>
        ))}
      </ul>
