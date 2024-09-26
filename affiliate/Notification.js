import './Notification.css'; // Adjust the path if necessary
import React from 'react';

const Notification = ({ message }) => (
    <div className="notification">
        {message}
    </div>
);

export default Notification;
