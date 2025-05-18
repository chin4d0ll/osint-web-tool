import logging
from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

from db import get_db_connection, init_db
from scrapers.twitter import scrape_twitter_profile

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
CORS(app)


@app.route("/api/social_footprint", methods=["POST"])
def social_footprint():
    """Mock social footprint endpoint. Replace with real logic per platform."""
    data = request.get_json()
    platform = data.get("platform")
    username = data.get("username")
    if not platform or not username:
        return jsonify(
            {"error": "Missing 'platform' or 'username' in request"}
        ), 400
    mock_result = {
        "platform": platform,
        "username": username,
        "profile_url": f"https://{platform}.com/{username}",
        "name": "John Doe",
        "bio": "This is a mock bio.",
        "location": "Bangkok, Thailand",
        "work": "Software Engineer",
        "education": "Chulalongkorn University",
        "connections": 1234,
        "public_posts": [
            {
                "content": "Hello world!",
                "hashtags": ["#osint"],
                "location": "Bangkok",
                "language": "en",
            },
            {
                "content": "Security tips",
                "hashtags": ["#security"],
                "location": "Bangkok",
                "language": "en",
            },
        ],
        "risk": {
            "phone_found": False,
            "email_found": True,
            "address_found": False,
            "privacy_score": 75,
        },
    }
    return jsonify({"result": mock_result})


@app.route("/api/risk_assessment", methods=["POST"])
def risk_assessment():
    """Mock risk assessment endpoint. Replace with real risk analysis logic."""
    data = request.get_json()
    target = data.get("target")
    if not target:
        return jsonify({"error": "Missing 'target' in request"}), 400
    mock_result = {
        "target": target,
        "risk_score": 82,
        "summary": (
            "Personal data leak detected and high risk from social media usage."
        ),
        "details": [
            "Email found in public posts",
            "Low privacy settings detected",
            "Data found in breach database",
        ],
    }
    return jsonify({"result": mock_result})


@app.route("/api/commercial", methods=["POST"])
def commercial_api():
    """Mock commercial API endpoint. Replace with real commercial logic."""
    api_key = request.headers.get("x-api-key")
    if not api_key or api_key != "demo-key":
        return jsonify({"error": "Invalid or missing API key"}), 401
    data = request.get_json()
    query = data.get("query")
    mock_result = {
        "query": query,
        "status": "success",
        "data": {"info": "This is a mock response from the commercial API."},
    }
    return jsonify({"result": mock_result})


@app.route("/", methods=["GET"])
def home():
    return "Hello from OSINT Tool Backend!"


@app.route("/db_test", methods=["GET"])
def db_test():
    conn = get_db_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT version();")
            db_version = cur.fetchone()
            cur.close()
            conn.close()
            return jsonify(
                {
                    "message": "Successfully connected to database!",
                    "db_version": db_version,
                }
            )
        except Exception as e:
            return (
                jsonify(
                    {
                        "message": (
                            "Database connection successful, but query failed."
                        ),
                        "error": str(e),
                    }
                ),
                500,
            )
    else:
        return jsonify({"message": "Failed to connect to database."}), 500


@app.route("/ip_lookup", methods=["GET"])
def ip_lookup():
    ip_address = request.args.get("ip")
    if not ip_address:
        return jsonify({"error": "IP address is required"}), 400
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except requests.exceptions.HTTPError as errh:
        logging.error(f"Http Error: {errh}")
        return jsonify({"error": f"Http Error: {errh}"}), 500
    except requests.exceptions.ConnectionError as errc:
        logging.error(f"Error Connecting: {errc}")
        return jsonify({"error": f"Error Connecting: {errc}"}), 500
    except requests.exceptions.Timeout as errt:
        logging.error(f"Timeout Error: {errt}")
        return jsonify({"error": f"Timeout Error: {errt}"}), 500
    except requests.exceptions.RequestException as err:
        logging.error(f"Something went wrong: {err}")
        return jsonify({"error": f"Something went wrong: {err}"}), 500


@app.route("/scrape_twitter_profile", methods=["GET"])
def scrape_twitter_profile_route():
    """Scrape Twitter profile data for a given username."""
    username = request.args.get("username")
    if not username:
        return jsonify({"error": "Twitter username is required"}), 400
    profile_data = scrape_twitter_profile(username)
    return jsonify(profile_data)


@app.route("/api/search", methods=["POST"])
def handle_search():
    data = request.get_json()
    search_type = data.get("type")
    search_value = data.get("value")
    if not isinstance(search_type, str) or not isinstance(search_value, str) or \
       not search_type.strip() or not search_value.strip():
        return jsonify({"error": "Missing 'type' or 'value' in request"}), 400
    mock_result = {
        "username": search_value if search_type == "username" else None,
        "email": search_value if search_type == "email" else None,
        "ip": search_value if search_type == "ip" else None,
        "social_profiles": [
            {
                "platform": "Facebook",
                "found": True,
                "url": f"https://facebook.com/{search_value}",
            },
            {"platform": "Twitter", "found": False, "url": None},
            {
                "platform": "Instagram",
                "found": True,
                "url": f"https://instagram.com/{search_value}",
            },
        ],
        "risk_score": 42,
        "breach_found": True,
        "breach_sources": ["HaveIBeenPwned", "Dehashed"],
    }
    return jsonify(
        {
            "message": "Search completed (mock)",
            "search_type": search_type,
            "search_value": search_value,
            "result": mock_result,
        }
    )


@app.errorhandler(Exception)
def handle_exception(e):
    logging.error(f"Internal server error: {e}")
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    logging.info("Attempting to initialize database schema...")
    init_db()
    logging.info("Starting Flask backend server...")
    app.run(host="0.0.0.0", port=5001)  # เปลี่ยนพอร์ตเป็น 5001
