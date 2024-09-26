// affiliate/affiliateRoutes.js
const express = require('express');
const router = express.Router();
const Affiliate = require('./affiliateModel');

// Route for registering as an affiliate
router.post('/register', async (req, res) => {
    try {
        const { userId, referralCode } = req.body;
        const newAffiliate = new Affiliate({ userId, referralCode });
        await newAffiliate.save();
        res.status(201).json(newAffiliate);
    } catch (error) {
        res.status(500).json({ message: 'Error registering affiliate', error });
    }
});

// Route for getting affiliate earnings
router.get('/:id/earnings', async (req, res) => {
    try {
        const affiliate = await Affiliate.findById(req.params.id);
        res.status(200).json({ earnings: affiliate.earnings });
    } catch (error) {
        res.status(500).json({ message: 'Error fetching earnings', error });
    }
});

module.exports = router;
