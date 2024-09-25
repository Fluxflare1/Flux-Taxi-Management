import React, { useState, useEffect } from 'react';
import axios from 'axios';

const SubscriptionPlans = () => {
  const [plans, setPlans] = useState([]);

  useEffect(() => {
    // Fetch available plans
    axios.get('/api/plans/')
      .then(response => {
        setPlans(response.data);
      })
      .catch(error => {
        console.error("Error fetching plans", error);
      });
  }, []);

  const subscribeToPlan = (planId) => {
    axios.post(`/api/subscriptions/`, { plan: planId })
      .then(response => {
        alert("Subscribed successfully!");
      })
      .catch(error => {
        console.error("Error subscribing to plan", error);
      });
  };

  return (
    <div>
      <h2>Subscription Plans</h2>
      <ul>
        {plans.map(plan => (
          <li key={plan.id}>
            {plan.name} - ${plan.price} for {plan.duration} days
            <button onClick={() => subscribeToPlan(plan.id)}>Subscribe</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default SubscriptionPlans;
