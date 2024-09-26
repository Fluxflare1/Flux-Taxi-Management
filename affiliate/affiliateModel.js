// affiliate/affiliateModel.js
const mongoose = require('mongoose');

const affiliateSchema = new mongoose.Schema({
    userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
    referralCode: { type: String, unique: true },
    earnings: { type: Number, default: 0 },
    referrals: [{ type: mongoose.Schema.Types.ObjectId, ref: 'User' }]
});

module.exports = mongoose.model('Affiliate', affiliateSchema);
