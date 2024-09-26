const mongoose = require('mongoose');

const affiliateSchema = new mongoose.Schema({
    email: { type: String, required: true, unique: true },
    // Add commission fields
    totalEarnings: { type: Number, default: 0 },
    // other fields...
});

const Affiliate = mongoose.model('Affiliate', affiliateSchema);
module.exports = Affiliate;
const crypto = require('crypto');

// Inside the Affiliate schema definition
const affiliateSchema = new mongoose.Schema({
    userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
    referralCode: { type: String, unique: true, default: () => crypto.randomBytes(4).toString('hex') }, // Unique code
    earnings: { type: Number, default: 0 },
    referrals: [{ type: mongoose.Schema.Types.ObjectId, ref: 'User' }]
});
// affiliate/affiliateModel.js
const mongoose = require('mongoose');

const affiliateSchema = new mongoose.Schema({
    userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
    referralCode: { type: String, unique: true },
    earnings: { type: Number, default: 0 },
    referrals: [{ type: mongoose.Schema.Types.ObjectId, ref: 'User' }]
});

module.exports = mongoose.model('Affiliate', affiliateSchema);
