import React, { useState } from 'react';

function SocialMediaAnalysis() {
  const [platform, setPlatform] = useState('twitter');
  const [username, setUsername] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setResult(null);
    try {
      const res = await fetch('/api/social_footprint', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ platform, username }),
      });
      if (!res.ok) throw new Error('API error');
      const data = await res.json();
      setResult(data.result);
    } catch (err) {
      setError('An error occurred while searching.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h3>Social Media Footprint Analysis</h3>
      <form onSubmit={handleSubmit} style={{ marginBottom: 24 }}>
        <label>
          Platform:
          <select
            value={platform}
            onChange={(e) => setPlatform(e.target.value)}
            style={{ marginLeft: 8 }}
          >
            <option value="twitter">Twitter/X</option>
            <option value="facebook">Facebook</option>
            <option value="instagram">Instagram</option>
            <option value="linkedin">LinkedIn</option>
          </select>
        </label>
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          placeholder="Enter username or profile id"
          style={{ marginLeft: 12, padding: 4, width: 220 }}
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
          <div style={{ marginBottom: 12 }}>
            <b>Platform:</b> {result.platform}
            <br />
            <b>Username:</b> {result.username}
            <br />
            <b>Profile URL:</b>{' '}
            <a href={result.profile_url} target="_blank" rel="noopener noreferrer">
              {result.profile_url}
            </a>
            <br />
            <b>Name:</b> {result.name}
            <br />
            <b>Bio:</b> {result.bio}
            <br />
            <b>Location:</b> {result.location}
            <br />
            <b>Work:</b> {result.work}
            <br />
            <b>Education:</b> {result.education}
            <br />
            <b>Connections:</b> {result.connections}
          </div>
          <div style={{ marginBottom: 12 }}>
            <b>Public Posts:</b>
            <ul>
              {result.public_posts &&
                result.public_posts.map((post, idx) => (
                  <li key={idx}>
                    <b>Content:</b> {post.content}
                    <br />
                    <b>Hashtags:</b> {post.hashtags.join(', ')}
                    <br />
                    <b>Location:</b> {post.location}
                    <br />
                    <b>Language:</b> {post.language}
                  </li>
                ))}
            </ul>
          </div>
          <div>
            <b>Risk Analysis:</b>
            <ul>
              <li>Phone found: {result.risk.phone_found ? 'Yes' : 'No'}</li>
              <li>Email found: {result.risk.email_found ? 'Yes' : 'No'}</li>
              <li>Address found: {result.risk.address_found ? 'Yes' : 'No'}</li>
              <li>
                Privacy Score: <b>{result.risk.privacy_score}</b>
              </li>
            </ul>
          </div>
        </div>
      )}
    </div>
  );
}

export default SocialMediaAnalysis;
