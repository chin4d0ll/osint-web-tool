# OSINT Tool Backend

This directory contains the Python Flask backend application for the OSINT Web Tool. It handles API requests, performs OSINT data collection and analysis, and interacts with the database.

## Prerequisites

- Python 3.9+
- pip (Python package installer)
- A virtual environment manager (e.g., `venv`)

## Setup and Installation

1.  **Navigate to the backend directory:**

    ```bash
    cd backend
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

    _(On Windows, use `.venv\Scripts\activate`)_

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Backend Server

Once the setup is complete and the virtual environment is activated, you can start the Flask development server:

```bash
python app.py
```

The backend API will typically be available at `http://localhost:5001` (or as configured).

## Project Structure

- `app.py`: The main Flask application file, containing API routes and core logic.
- `requirements.txt`: A list of Python dependencies for the backend.
- `.venv/`: (If created) The Python virtual environment directory (should be in `.gitignore`).
- (Other modules/folders for database models, services, utilities etc. can be added here)

## API Endpoints

(Document your API endpoints here as they are developed. For example:)

- `GET /api/example`: Description of what this endpoint does.
- `POST /api/submit_data`: Description and expected request body.
