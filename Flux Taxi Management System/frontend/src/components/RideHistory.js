import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './RideHistory.css'; // Assuming you create a CSS file for styling

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

  const formatDate = (dateString) => {
    const options = { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' };
    return new Date(dateString).toLocaleDateString('en-US', options);
  };

  return (
    <div className="ride-history">
      <h2>Ride History</h2>
      {history.length === 0 ? (
        <p>No ride history available.</p>
      ) : (
        <ul>
          {history.map(ride => (
            <li key={ride.id} className="ride-item">
              <div>
                <strong>Pickup:</strong> {ride.ride.pickup_location} <br />
                <strong>Dropoff:</strong> {ride.ride.dropoff_location} <br />
                <strong>Completed At:</strong> {formatDate(ride.completed_at)} <br />
                <strong>Fare:</strong> ${ride.fare_amount} <br />
                <strong>Status:</strong> {ride.ride.status} <br />
                {ride.driver_rating && (
                  <span>Rating: {ride.driver_rating}/5</span>
                )}
              </div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default RideHistory;
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
            {ride.ride.pickup_location} to {ride.ride.dropoff_location} - Completed at: {ride.completed_at}
            {ride.driver_rating && (
              <span> | Rating: {ride.driver_rating}/5</span>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default RideHistory;
