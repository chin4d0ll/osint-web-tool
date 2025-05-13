
import React, { useState } from 'react';
import './CommercialApi.css';

function CommercialApi() {
  const [apiKey, setApiKey] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const callCommercialApi = async (key) => {
    const res = await fetch('/api/commercial', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'x-api-key': key },
      body: JSON.stringify({ query: 'test' })
    });
    if (!res.ok) throw new Error('API error');
    return res.json();
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (apiKey.length < 10) {
      setError('API Key must be at least 10 characters long.');
      return;
    }
    setLoading(true);
    setError('');
    setResult(null);
    try {
      const data = await callCommercialApi(apiKey);
      setResult(data.result);
      setApiKey(''); // Clear the API key
    } catch (err) {
      setError(err.message || 'An error occurred while calling the Commercial API.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h3>Commercial API Service</h3>
      <p>API for commercial OSINT and subscription services</p>
      <form onSubmit={handleSubmit} style={{ marginBottom: 24 }}>
        <input
          type="text"
          value={apiKey}
          onChange={e => setApiKey(e.target.value)}
          placeholder="Enter API Key"
          className="input"
          required
        />
        <button
          type="submit"
          className="button"
          disabled={loading}
          aria-busy={loading}
        >
          {loading ? 'Testing...' : 'Test API'}
        </button>
      </form>
      {error && <div style={{ color: 'red' }}>{error}</div>}
      {result && (
        <div className="result">
          <h4>Result from Commercial API</h4>
          <pre style={{ whiteSpace: 'pre-wrap', wordBreak: 'break-all' }}>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
      <div style={{ marginTop: 32 }}>
        <b>API Usage Example:</b>
        <pre className="api-usage">
{`POST /api/commercial\nHeaders: { 'x-api-key': 'YOUR_API_KEY' }\nBody: { "query": "test" }\n`}
        </pre>
      </div>
    </div>
  );
}

export default CommercialApi;
