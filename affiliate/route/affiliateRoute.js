const express = require('express');
const AffiliateController = require('../controllers/AffiliateController');

const router = express.Router();

router.post('/register', AffiliateController.registerAffiliate);

// More routes can be added for performance tracking, payout requests, etc.

module.exports = router;
