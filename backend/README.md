# OSINT Tool Backend

This is the Python Flask backend for the OSINT Web Tool. It exposes RESTful APIs for data collection, analysis, and integration with the frontend.

## Requirements
- Python 3.9+
- pip

## Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the API
```bash
python app.py
```
The API will be available at http://localhost:5001

## Project Structure
- `app.py` — Main Flask app and API routes
- `requirements.txt` — Python dependencies
- `test_app.py` — Basic tests

## Example Endpoint
- `GET /` — Health check or welcome message

## Testing
```bash
pytest
```
