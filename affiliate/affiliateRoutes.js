router.post('/promote-service', promoteService);
// ... existing imports
const { registerAffiliate, getReferralLink } = require('./affiliateController');

router.post('/register', registerAffiliate);
router.get('/:affiliateId/referral-link', getReferralLink);
const express = require('express');
const { registerAffiliate, getReferralLink } = require('./affiliateController');

const router = express.Router();

// Route for registering an affiliate
router.post('/register', registerAffiliate);

// Route for getting the referral link
router.get('/:affiliateId/referral-link', getReferralLink);

module.exports = router;
// Route for fetching referral statistics
router.get('/:id/stats', async (req, res) => {
    try {
        const affiliate = await Affiliate.findById(req.params.id).populate('referrals');
        res.status(200).json({ earnings: affiliate.earnings, referrals: affiliate.referrals });
    } catch (error) {
        res.status(500).json({ message: 'Error fetching stats', error });
    }
});
// Route to update earnings
router.post('/:id/earnings', async (req, res) => {
    try {
        const { earnings } = req.body;
        const affiliate = await Affiliate.findById(req.params.id);
        affiliate.earnings += earnings; // Update earnings
        await affiliate.save();
        res.status(200).json({ earnings: affiliate.earnings });
    } catch (error) {
        res.status(500).json({ message: 'Error updating earnings', error });
    }
});
// affiliate/affiliateRoutes.js
const express = require('express');
const { check, validationResult } = require('express-validator');
const router = express.Router();
const Affiliate = require('./affiliateModel');

// Route for registering as an affiliate
router.post('/register', [
    check('userId').isMongoId().withMessage('User ID must be valid'),
    check('referralCode').isString().withMessage('Referral code must be a string')
], async (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array() });
    }

    try {
        const { userId, referralCode } = req.body;
        const newAffiliate = new Affiliate({ userId, referralCode });
        await newAffiliate.save();
        res.status(201).json(newAffiliate);
    } catch (error) {
        res.status(500).json({ message: 'Error registering affiliate', error });
    }
});
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
