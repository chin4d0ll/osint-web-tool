
import './App.css';
import React, { useState } from 'react';

function App() {
  const [type, setType] = useState('username');
  const [value, setValue] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setResult(null);
    try {
      const res = await fetch('/api/search', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ type, value })
      });
      if (!res.ok) throw new Error('API error');
      const data = await res.json();
      setResult(data.result);
    } catch (err) {
      setError('เกิดข้อผิดพลาดในการค้นหา');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App" style={{ maxWidth: 600, margin: '2rem auto', fontFamily: 'sans-serif' }}>
      <h2>OSINT Web Tool</h2>
      <form onSubmit={handleSubmit} style={{ marginBottom: 24 }}>
        <label>
          ประเภทข้อมูล:
          <select value={type} onChange={e => setType(e.target.value)} style={{ marginLeft: 8 }}>
            <option value="username">Username</option>
            <option value="email">Email</option>
            <option value="ip">IP Address</option>
          </select>
        </label>
        <input
          type="text"
          value={value}
          onChange={e => setValue(e.target.value)}
          placeholder="กรอกข้อมูลที่ต้องการค้นหา"
          style={{ marginLeft: 12, padding: 4, width: 220 }}
          required
        />
        <button type="submit" style={{ marginLeft: 12, padding: '4px 16px' }} disabled={loading}>
          {loading ? 'กำลังค้นหา...' : 'ค้นหา'}
        </button>
      </form>
      {error && <div style={{ color: 'red' }}>{error}</div>}
      {result && (
        <div style={{ background: '#f6f6f6', padding: 16, borderRadius: 8 }}>
          <h3>ผลลัพธ์</h3>
          {result.username && <div><b>Username:</b> {result.username}</div>}
          {result.email && <div><b>Email:</b> {result.email}</div>}
          {result.ip && <div><b>IP:</b> {result.ip}</div>}
          <div><b>Risk Score:</b> {result.risk_score}</div>
          <div><b>Breach Found:</b> {result.breach_found ? 'Yes' : 'No'}</div>
          {result.breach_sources && result.breach_sources.length > 0 && (
            <div><b>Breach Sources:</b> {result.breach_sources.join(', ')}</div>
          )}
          <div style={{ marginTop: 8 }}>
            <b>Social Profiles:</b>
            <ul>
              {result.social_profiles.map((profile, idx) => (
                <li key={idx}>
                  {profile.platform}: {profile.found ? (
                    <a href={profile.url} target="_blank" rel="noopener noreferrer">พบ</a>
                  ) : 'ไม่พบ'}
                </li>
              ))}
            </ul>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
