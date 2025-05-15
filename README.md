# OSINT Web Tool

A modern Open Source Intelligence (OSINT) platform for gathering and analyzing public data. This project features a Python Flask backend and a React frontend, containerized with Docker for easy deployment.

## Project Structure

- `backend/` — Python Flask API for OSINT data collection and analysis
- `frontend/` — React web UI for user interaction
- `docker-compose.yml` — Multi-service orchestration (backend, frontend, database)

## Quick Start (with Docker)

1. Clone the repository:
   ```bash
   git clone https://github.com/chin4d0ll/osint-web-tool.git
   cd osint-web-tool
   ```
2. Build and run all services:
   ```bash
   docker-compose up --build
   ```
3. Access the app:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:5001

## Manual Development Setup
- See [`backend/README.md`](backend/README.md) for backend setup
- See [`frontend/README.md`](frontend/README.md) for frontend setup

## Contributing
Pull requests are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

## License
MIT License — see [LICENSE](LICENSE)
