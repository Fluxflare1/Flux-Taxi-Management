const Affiliate = require('./affiliateModel');

// Register a new affiliate
const registerAffiliate = async (req, res) => {
    const { email } = req.body;
    try {
        const newAffiliate = new Affiliate({ email });
        await newAffiliate.save();
        res.status(201).json(newAffiliate);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// Get unique referral link
const getReferralLink = async (req, res) => {
    const affiliateId = req.params.affiliateId;
    const referralLink = `https://yourdomain.com/register?ref=${affiliateId}`;
    res.status(200).json({ referralLink });
};

module.exports = { registerAffiliate, getReferralLink };
