import React, { useState, useEffect } from 'react';
import axios from 'axios';

const UserSubscriptionDashboard = () => {
  const [subscriptions, setSubscriptions] = useState([]);

  useEffect(() => {
    // Fetch user's subscriptions
    axios.get('/api/subscriptions/')
      .then(response => {
        setSubscriptions(response.data);
      })
      .catch(error => {
        console.error("Error fetching subscriptions", error);
      });
  }, []);

  return (
    <div>
      <h2>Your Subscriptions</h2>
      <ul>
        {subscriptions.map(subscription => (
          <li key={subscription.id}>
            {subscription.plan.name} - Active until {new Date(subscription.end_date).toLocaleDateString()}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default UserSubscriptionDashboard;
