# OSINT Web Tool 🌐

**A web-based tool for Open Source Intelligence (OSINT) gathering, enabling users to extract and analyze publicly available data for research, investigations, or cybersecurity.**

---

## 🚀 Features
- **Data Extraction:** Gather information from multiple OSINT sources automatically.
- **Data Analysis:** Analyze publicly available data for insights and correlations.
- **Customizable Plugins:** Add new data sources or extend functionality easily with Python.
- **Multi-Platform Support:** Works on Linux, macOS, and Windows.
- **Multi-Language UI:** Supports both Thai 🇹🇭 and English.

---

## 📖 Documentation
### **Getting Started**
1. **Clone the repository:**
   ```bash
   git clone https://github.com/chin4d0ll/osint-web-tool.git
   cd osint-web-tool
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```bash
   python app.py
   ```

### **Using Codespaces**
1. Open the repository in GitHub Codespaces.
2. The environment will automatically install all dependencies for the backend and frontend.
3. Ports `5000` (backend) and `3000` (frontend) will be forwarded automatically.

### **Manual Setup**
1. **Backend**
   ```bash
   cd backend
   pip install -r requirements.txt
   python app.py
   ```

2. **Frontend**
   ```bash
   cd frontend
   npm install
   npm start
   ```

---

## 🔄 Updates
- **May 2025**: Added automated setup for Codespaces with `devcontainer.json`.
- **April 2025**: Improved Docker support for frontend and backend.

---

## System Requirements

- **Python Version:** 3.8 or higher
- **Dependencies:** Listed in requirements.txt
- **Browser:** A modern browser for the web interface (e.g., Chrome, Firefox)

## Supported OSINT Sources

- Social Media Platforms
- Public Databases
- Domain and IP Lookup
- Custom APIs (extendable)

## 🔧 How to Use

1. **Run the tool:**
   - Open your browser and navigate to `http://127.0.0.1:5000`.
2. **Start a new scan:**
   - Enter a target (e.g., domain, IP, username).
3. **View results:**
   - Analyze the collected data directly from the dashboard.
4. **Export data:**
   - Save results as CSV or JSON for further analysis.

---

## 🛠️ Development

### **Contributing**

We welcome contributions from the community! To get started:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed explanation.

### **Testing**

To ensure everything works as expected:

```bash
python -m unittest discover tests
```

---

## ⚠️ Disclaimer

This tool is designed for educational purposes only. Do not use it for illegal activities. The developers are not responsible for any misuse of this tool.

## 📬 Contact & Support

If you have any questions or feedback

- **GitHub Issues:** Submit here
- **Email:** chin4d0ll@example.com

---

## ❤️ Support Us

If you find this tool helpful:

- 🌟 Star the repo
- 🛠️ Contribute your code
- ☕ Buy us a coffee (coming soon!)
