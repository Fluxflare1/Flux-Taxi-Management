const express = require('express');
const mongoose = require('mongoose');
const affiliateModule = require('./affiliate');

const app = express();
app.use(express.json());

// Other middleware and routes...

app.use('/api', affiliateModule);

// Connect to MongoDB and start server...
