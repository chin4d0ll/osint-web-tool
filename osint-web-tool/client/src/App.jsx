import React, { useState } from "react";
import axios from "axios";

function App() {
  const [platform, setPlatform] = useState("github");
  const [username, setUsername] = useState("");
  const [result, setResult] = useState(null);

  const handleSearch = async () => {
    try {
      const res = await axios.post("/api/social_footprint", {
        platform,
        username,
      });
      setResult(res.data.result);
    } catch (err) {
      alert("Error: " + err.response?.data?.error || err.message);
    }
  };

  const handleExport = async () => {
    const url = `/api/export/${username}`;
    window.open(url, "_blank");
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "sans-serif" }}>
      <h2>OSINT Web Tool</h2>
      <select value={platform} onChange={(e) => setPlatform(e.target.value)}>
        <option value="github">GitHub</option>
        <option value="instagram">Instagram</option>
        <option value="twitter">Twitter</option>
      </select>
      <input
        type="text"
        placeholder="Enter username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        style={{ marginLeft: "1rem" }}
      />
      <button onClick={handleSearch} style={{ marginLeft: "1rem" }}>
        Search
      </button>
      <button onClick={handleExport} style={{ marginLeft: "1rem" }}>
        Export
      </button>

      {result && (
        <div style={{ marginTop: "2rem" }}>
          <h3>Result:</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;