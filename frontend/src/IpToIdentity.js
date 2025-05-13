import React, { useState } from 'react';

function IpToIdentity() {
  const [ip, setIp] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setResult(null);
    try {
      const res = await fetch(`/ip_lookup?ip=${encodeURIComponent(ip)}`);
      if (!res.ok) throw new Error('API error');
      const data = await res.json();
      setResult(data);
    } catch (err) {
      setError('An error occurred while searching for IP.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h3>IP-to-Identity Analysis</h3>
      <form onSubmit={handleSubmit} style={{ marginBottom: 24 }}>
        <input
          type="text"
          value={ip}
          onChange={e => setIp(e.target.value)}
          placeholder="Enter IP Address"
          style={{ padding: 4, width: 220 }}
          required
        />
        <button type="submit" style={{ marginLeft: 12, padding: '4px 16px' }} disabled={loading}>
          {loading ? 'Searching...' : 'Search'}
        </button>
      </form>
      {error && <div style={{ color: 'red' }}>{error}</div>}
      {result && (
        <div style={{ background: '#f6f6f6', padding: 16, borderRadius: 8 }}>
          <h4>Result</h4>
          <div><b>IP:</b> {result.ip}</div>
          <div><b>City:</b> {result.city}</div>
          <div><b>Region:</b> {result.region}</div>
          <div><b>Country:</b> {result.country}</div>
          <div><b>Location:</b> {result.loc}</div>
          <div><b>Org:</b> {result.org}</div>
          <div><b>Timezone:</b> {result.timezone}</div>
        </div>
      )}
    </div>
  );
}

export default IpToIdentity;
