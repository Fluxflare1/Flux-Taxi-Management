import React, { useState } from 'react';
import axios from 'axios';

const ReferralTracking = () => {
    const [affiliateId, setAffiliateId] = useState('');
    const [earnings, setEarnings] = useState(null);

    const handleGetEarnings = async () => {
        try {
            const response = await axios.get(`/api/affiliate/earnings/${affiliateId}`);
            setEarnings(response.data.earnings);
        } catch (error) {
            console.error('Error fetching earnings:', error);
        }
    };

    return (
        <div>
            <h2>Check Your Earnings</h2>
            <input
                type="text"
                value={affiliateId}
                onChange={(e) => setAffiliateId(e.target.value)}
                placeholder="Enter your Affiliate ID"
            />
            <button onClick={handleGetEarnings}>Get Earnings</button>
            {earnings !== null && (
                <div>Your Earnings: {earnings}</div>
            )}
        </div>
    );
};

export default ReferralTracking;
