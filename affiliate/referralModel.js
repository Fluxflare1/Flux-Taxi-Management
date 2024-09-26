const mongoose = require('mongoose');

// Define the referral schema
const referralSchema = new mongoose.Schema({
    affiliateId: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Affiliate', // Reference to the Affiliate model
        required: true,
    },
    referredUserId: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'User', // Reference to the User model
        required: true,
    },
    createdAt: {
        type: Date,
        default: Date.now, // Set the default value to the current date
    }
});

// Export the Referral model
module.exports = mongoose.model('Referral', referralSchema);
