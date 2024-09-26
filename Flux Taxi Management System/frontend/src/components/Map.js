// frontend/src/components/Map.js
import React, { useState, useEffect } from 'react';

const Map = ({ driverLocation }) => {
    const [map, setMap] = useState(null);
    const [marker, setMarker] = useState(null);

    useEffect(() => {
        const mapInstance = new google.maps.Map(document.getElementById('map'), {
            zoom: 10,
            center: driverLocation,
        });
        setMap(mapInstance);

        const markerInstance = new google.maps.Marker({
            position: driverLocation,
            map: mapInstance,
        });
        setMarker(markerInstance);
    }, [driverLocation]);

    useEffect(() => {
        if (marker) {
            marker.setPosition(driverLocation);
        }
    }, [driverLocation]);

    return <div id="map" style={{ height: '400px', width: '100%' }} />;
};

export default Map;
