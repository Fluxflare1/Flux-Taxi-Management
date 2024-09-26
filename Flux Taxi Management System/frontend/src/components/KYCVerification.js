import React, { useState } from 'react';

const KYCVerification = () => {
    const [document, setDocument] = useState(null);

    const handleVerifyKYC = () => {
        const formData = new FormData();
        formData.append('document', document);

        fetch('/api/verify_kyc', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => alert(data.status));
    };

    return (
        <div>
            <input type="file" onChange={(e) => setDocument(e.target.files[0])} />
            <button onClick={handleVerifyKYC}>Verify KYC</button>
        </div>
    );
};

export default KYCVerification;
