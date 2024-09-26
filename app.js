// app.js
const express = require('express');
const mongoose = require('mongoose');
const affiliateRoutes = require('./affiliate'); // This now points to your affiliate module

const app = express();
app.use(express.json());

// Other middleware and routes...

app.use('/api/affiliate', affiliateRoutes); // Mount affiliate routes

// Connect to MongoDB
mongoose.connect('your_mongo_db_connection_string', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => {
        app.listen(3000, () => {
            console.log('Server is running on port 3000');
        });
    })
    .catch(error => console.error('MongoDB connection error:', error));

