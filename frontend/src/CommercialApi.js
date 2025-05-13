import React, { useState } from 'react';

function CommercialApi() {
  const [apiKey, setApiKey] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setResult(null);
    try {
      // ตัวอย่าง mock API call
      const res = await fetch('/api/commercial', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'x-api-key': apiKey },
        body: JSON.stringify({ query: 'test' })
      });
      if (!res.ok) throw new Error('API error');
      const data = await res.json();
      setResult(data.result);
    } catch (err) {
      setError('เกิดข้อผิดพลาดในการเรียกใช้ Commercial API');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h3>Commercial API Service</h3>
      <p>API สำหรับบริการ OSINT เชิงพาณิชย์และ subscription</p>
      <form onSubmit={handleSubmit} style={{ marginBottom: 24 }}>
        <input
          type="text"
          value={apiKey}
          onChange={e => setApiKey(e.target.value)}
          placeholder="กรอก API Key"
          style={{ padding: 4, width: 220 }}
          required
        />
        <button type="submit" style={{ marginLeft: 12, padding: '4px 16px' }} disabled={loading}>
          {loading ? 'กำลังทดสอบ...' : 'ทดสอบ API'}
        </button>
      </form>
      {error && <div style={{ color: 'red' }}>{error}</div>}
      {result && (
        <div style={{ background: '#f6f6f6', padding: 16, borderRadius: 8 }}>
          <h4>ผลลัพธ์จาก Commercial API</h4>
          <pre style={{ whiteSpace: 'pre-wrap', wordBreak: 'break-all' }}>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
      <div style={{ marginTop: 32 }}>
        <b>API Usage Example:</b>
        <pre style={{ background: '#eee', padding: 12, borderRadius: 8 }}>
{`POST /api/commercial\nHeaders: { 'x-api-key': 'YOUR_API_KEY' }\nBody: { "query": "test" }\n`}
        </pre>
      </div>
    </div>
  );
}

export default CommercialApi;
export default CommercialApi;
