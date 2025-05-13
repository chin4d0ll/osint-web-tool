import './App.css';
import React, { useState } from 'react';
import Dashboard from './Dashboard';
import SocialMediaAnalysis from './SocialMediaAnalysis';
import IpToIdentity from './IpToIdentity';
import RiskAssessment from './RiskAssessment';
import CommercialApi from './CommercialApi';

function App() {
  const [page, setPage] = useState('dashboard');

  return (
    <div className="App" style={{ maxWidth: 800, margin: '2rem auto', fontFamily: 'sans-serif' }}>
      <h2>OSINT Web Tool</h2>
      <nav style={{ marginBottom: 24 }}>
        <button onClick={() => setPage('dashboard')} style={{ marginRight: 8 }}>
          Dashboard
        </button>
        <button onClick={() => setPage('social')}>Social Media Analysis</button>
        <button onClick={() => setPage('ip')}>IP-to-Identity</button>
        <button onClick={() => setPage('risk')}>Risk Assessment</button>
        <button onClick={() => setPage('commercial')}>Commercial API</button>
      </nav>
      {page === 'dashboard' && <Dashboard />}
      {page === 'social' && <SocialMediaAnalysis />}
      {page === 'ip' && <IpToIdentity />}
      {page === 'risk' && <RiskAssessment />}
      {page === 'commercial' && <CommercialApi />}
    </div>
  );
}

export default App;
