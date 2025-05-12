# OSINT Web Tool

An Open Source Intelligence (OSINT) web-based tool designed to gather and analyze publicly available information. This project consists of a Python Flask backend and a React frontend.

## Project Structure

- `/backend`: Contains the Python Flask application, API endpoints, and logic for OSINT data collection and processing.
- `/frontend`: Contains the React application for the user interface.
- `/docker-compose.yml`: Defines the services for running the application (e.g., backend, frontend, database).
- `/.devcontainer`: Contains configurations for developing in a Dev Container or GitHub Codespaces.

## Technologies Used

- **Backend**: Python, Flask, Selenium, PostgreSQL (or other as configured)
- **Frontend**: React, JavaScript/TypeScript, HTML, CSS
- **Containerization**: Docker

## Getting Started

### Prerequisites

- Docker Desktop (or Docker Engine)
- Git

### Development Environment

This project is configured to run in a [Dev Container](https://code.visualstudio.com/docs/remote/containers) or [GitHub Codespaces](https://github.com/features/codespaces).

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd osint-web-tool
    ```
2.  **Open in Dev Container/Codespaces:**
    - If using VS Code, it should prompt you to "Reopen in Container".
    - If using GitHub Codespaces, a pre-configured environment will be created for you.

### Manual Setup (Alternative)

Detailed instructions for manual setup of the backend and frontend can be found in their respective README files:

- [`backend/README.md`](backend/README.md)
- [`frontend/README.md`](frontend/README.md)

## Running the Application

(Instructions will depend on whether you are using Dev Containers, docker-compose directly, or running services manually. This section can be filled out in more detail later.)

## Contributing

(Details on how to contribute to the project, coding standards, etc.)

## License

(Specify the license for your project, e.g., MIT License)
