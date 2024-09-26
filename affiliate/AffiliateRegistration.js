import React, { useState } from 'react';
import axios from 'axios';

const AffiliateRegistration = () => {
    const [userId, setUserId] = useState('');

    const handleRegister = async () => {
        try {
            const response = await axios.post('/api/affiliate/register', { userId });
            console.log('Affiliate registered:', response.data);
        } catch (error) {
            console.error('Error registering affiliate:', error);
        }
    };

    return (
        <div>
            <h2>Register as an Affiliate</h2>
            <input
                type="text"
                value={userId}
                onChange={(e) => setUserId(e.target.value)}
                placeholder="Enter your User ID"
            />
            <button onClick={handleRegister}>Register</button>
        </div>
    );
};

export default AffiliateRegistration;
