const express = require('express');
const affiliateRoutes = require('./routes/affiliateRoutes');

const router = express.Router();

router.use('/affiliate', affiliateRoutes);

module.exports = router;
