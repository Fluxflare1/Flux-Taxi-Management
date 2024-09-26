import React from 'react';

const ReferralLink = ({ referralLink }) => (
    <div>
        <h2>Your Referral Link</h2>
        <p>{referralLink}</p>
        <button onClick={() => navigator.clipboard.writeText(referralLink)}>Copy Link</button>
    </div>
);

export default ReferralLink;
