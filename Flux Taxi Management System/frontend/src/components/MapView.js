import React, { useState, useEffect } from 'react';

function MapView() {
    const [map, setMap] = useState(null);

    useEffect(() => {
        const googleMapsScript = document.createElement('script');
        googleMapsScript.src = `https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places`;
        googleMapsScript.async = true;
        window.document.body.appendChild(googleMapsScript);

        googleMapsScript.addEventListener('load', () => {
            const map = new window.google.maps.Map(document.getElementById('map'), {
                center: { lat: -34.397, lng: 150.644 },
                zoom: 8,
            });
            setMap(map);
        });
    }, []);

    return <div id="map" style={{ height: '500px', width: '100%' }} />;
}

export default MapView;
