import React, { useState } from 'react';

function RiskAssessment() {
  const [target, setTarget] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setResult(null);
    try {
      const res = await fetch('/api/risk_assessment', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ target }),
      });
      if (!res.ok) throw new Error('API error');
      const data = await res.json();
      setResult(data.result);
    } catch (err) {
      setError('An error occurred during risk assessment.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h3>OSINT-Driven Risk Assessment Tool</h3>
      <form onSubmit={handleSubmit} style={{ marginBottom: 24 }}>
        <input
          type="text"
          value={target}
          onChange={(e) => setTarget(e.target.value)}
          placeholder="Enter username, email, or IP"
          style={{ padding: 4, width: 260 }}
          required
        />
        <button type="submit" style={{ marginLeft: 12, padding: '4px 16px' }} disabled={loading}>
          {loading ? 'Assessing...' : 'Assess'}
        </button>
      </form>
      {error && <div style={{ color: 'red' }}>{error}</div>}
      {result && (
        <div style={{ background: '#f6f6f6', padding: 16, borderRadius: 8 }}>
          <h4>Risk Assessment Result</h4>
          <div>
            <b>Target:</b> {result.target}
          </div>
          <div>
            <b>Risk Score:</b>{' '}
            <span style={{ color: result.risk_score > 70 ? 'red' : 'green' }}>
              {result.risk_score}
            </span>
          </div>
          <div>
            <b>Summary:</b> {result.summary}
          </div>
          <div>
            <b>Details:</b>
          </div>
          <ul>{result.details && result.details.map((item, idx) => <li key={idx}>{item}</li>)}</ul>
        </div>
      )}
    </div>
  );
}

export default RiskAssessment;
