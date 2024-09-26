import React, { useEffect, useState } from 'react';
import axios from 'axios';

const PerformanceDashboard = () => {
    const [performance, setPerformance] = useState(null);

    useEffect(() => {
        const fetchPerformance = async () => {
            const response = await axios.get('/api/affiliate/performance'); // Adjust endpoint
            setPerformance(response.data);
        };
        fetchPerformance();
    }, []);

    return (
        <div>
            {performance ? (
                <div>
                    <h1>Your Performance</h1>
                    <p>Total Earnings: {performance.totalEarnings}</p>
                    {/* Add more metrics */}
                </div>
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
};

export default PerformanceDashboard;
