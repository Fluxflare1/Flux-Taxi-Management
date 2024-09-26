import React, { useState } from 'react';
import axios from 'axios';

const DriverAvailability = ({ driverId }) => {
    const [selectedCompany, setSelectedCompany] = useState(null);
    
    const handleAvailabilityChange = async (companyId) => {
        try {
            const response = await axios.post('/api/driver/update-availability/', {
                driver_id: driverId,
                company_id: companyId,
            });
            alert('Availability updated');
        } catch (error) {
            console.error('Error updating availability', error);
        }
    };

    return (
        <div>
            <h1>Update Availability</h1>
            <select onChange={(e) => setSelectedCompany(e.target.value)}>
                {/* Populate taxi companies from API */}
                <option value={null}>Select Taxi Company</option>
                {/* Example */}
                <option value={1}>Taxi Company 1</option>
                <option value={2}>Taxi Company 2</option>
            </select>
            <button onClick={() => handleAvailabilityChange(selectedCompany)}>Update</button>
        </div>
    );
};

export default DriverAvailability;
