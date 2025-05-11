import './App.css';
import React, { useState } from 'react'; // Import useState

function App() {
  const [ipAddress, setIpAddress] = useState('');
  const [lookupResult, setLookupResult] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleLookup = async () => {
    if (!ipAddress) {
      setError('Please enter an IP address.');
      setLookupResult(null);
      return;
    }
    setLoading(true);
    setError('');
    setLookupResult(null);
    try {
      // Assuming backend is running on port 5001
      const response = await fetch(`http://localhost:5001/ip_lookup?ip=${ipAddress}`);
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || `HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      setLookupResult(data);
    } catch (e) {
      setError(e.message || 'Failed to fetch IP information.');
      setLookupResult(null);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>OSINT Tool - IP Lookup</h1>
        <div>
          <input
            type="text"
            value={ipAddress}
            onChange={(e) => setIpAddress(e.target.value)}
            placeholder="Enter IP Address (e.g., 8.8.8.8)"
            disabled={loading}
          />
          <button onClick={handleLookup} disabled={loading}>
            {loading ? 'Looking up...' : 'Lookup IP'}
          </button>
        </div>

        {error && <p style={{ color: 'red' }}>Error: {error}</p>}

        {lookupResult && (
          <div style={{ textAlign: 'left', marginTop: '20px', padding: '10px', border: '1px solid #ccc', borderRadius: '5px' }}>
            <h2>Lookup Result for {lookupResult.ip}</h2>
            <pre>{JSON.stringify(lookupResult, null, 2)}</pre>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
