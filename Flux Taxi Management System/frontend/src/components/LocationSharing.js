import React, { useState } from 'react';

const LocationSharing = () => {
    const [location, setLocation] = useState({latitude: '', longitude: ''});

    const handleShareLocation = () => {
        fetch('/api/share_location', {
            method: 'POST',
            body: JSON.stringify(location),
            headers: {
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => alert(data.status));
    };

    return (
        <div>
            <input type="text" placeholder="Latitude" onChange={(e) => setLocation({...location, latitude: e.target.value})} />
            <input type="text" placeholder="Longitude" onChange={(e) => setLocation({...location, longitude: e.target.value})} />
            <button onClick={handleShareLocation}>Share Location</button>
        </div>
    );
};

export default LocationSharing;
