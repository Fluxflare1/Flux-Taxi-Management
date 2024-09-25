import React, { useState, useEffect } from 'react';
import axios from 'axios';

const BillingHistory = () => {
  const [billing, setBilling] = useState([]);

  useEffect(() => {
    // Fetch user's billing history
    axios.get('/api/billing/')
      .then(response => {
        setBilling(response.data);
      })
      .catch(error => {
        console.error("Error fetching billing history", error);
      });
  }, []);

  return (
    <div>
      <h2>Billing History</h2>
      <ul>
        {billing.map(record => (
          <li key={record.transaction_id}>
            {record.amount} - {new Date(record.date).toLocaleDateString()} - {record.status}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default BillingHistory;
