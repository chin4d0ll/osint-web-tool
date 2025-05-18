# --- CLEANED IMPORTS ---
import os
import psycopg2
from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --- APP INIT ---
app = Flask(__name__)
CORS(app)


@app.route("/api/social_footprint", methods=["POST"])
def social_footprint():
    data = request.get_json()
    platform = data.get("platform")
    username = data.get("username")
    if not platform or not username:
        return jsonify({"error": "Missing 'platform' or 'username' in request"}), 400

    # MOCK: Replace with real API/scraping logic for each platform
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


# --- Risk Assessment Tool ---
@app.route("/api/risk_assessment", methods=["POST"])
def risk_assessment():
    data = request.get_json()
    target = data.get("target")
    if not target:
        return jsonify({"error": "Missing 'target' in request"}), 400

    # MOCK: Replace with real risk analysis logic
    mock_result = {
        "target": target,
        "risk_score": 82,
        "summary": "Personal data leak detected and high risk from social media usage.",
        "details": [
            "Email found in public posts",
            "Low privacy settings detected",
            "Data found in breach database",
        ],
    }
    return jsonify({"result": mock_result})


# --- Commercial API (mock) ---
@app.route("/api/commercial", methods=["POST"])
def commercial_api():
    api_key = request.headers.get("x-api-key")
    if not api_key or api_key != "demo-key":
        return jsonify({"error": "Invalid or missing API key"}), 401
    data = request.get_json()
    query = data.get("query")
    # MOCK: Replace with real commercial logic
    mock_result = {
        "query": query,
        "status": "success",
        "data": {"info": "This is a mock response from the commercial API."},
    }
    return jsonify({"result": mock_result})


import os
import psycopg2
from flask import Flask, jsonify, request  # Add request
from flask_cors import CORS
import requests  # Add requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Database connection details (should ideally be from environment variables in production)
DB_HOST = "db"  # This is the service name from docker-compose.yml
DB_NAME = "osintdb"
DB_USER = "osintuser"
# IMPORTANT: Use environment variables or secrets for production
DB_PASS = "osintpassword"


def get_db_connection():
    """Establishes a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL database: {e}")
        # In a real app, you might want to raise an exception or handle this more gracefully
        return None


@app.route("/")
def home():
    return "Hello from OSINT Tool Backend!"


@app.route("/db_test")
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
        except psycopg2.Error as e:
            return (
                jsonify(
                    {
                        "message": "Database connection successful, but query failed.",
                        "error": str(e),
                    }
                ),
                500,
            )
    else:
        return jsonify({"message": "Failed to connect to database."}), 500


# Example: Initialize database schema (run once or check if tables exist)


def init_db():
    conn = get_db_connection()
    if not conn:
        print("Could not connect to DB to initialize schema.")
        return

    try:
        cur = conn.cursor()
        # Example table - adjust to your needs for storing OSINT data
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS search_history (
                id SERIAL PRIMARY KEY,
                query TEXT NOT NULL,
                source VARCHAR(100), -- e.g., 'twitter', 'ipinfo'
                results JSONB,        -- Store results as JSON
                risk_score INTEGER,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
            );
        """
        )
        # Add more tables as needed (e.g., users, api_keys, reports)
        # cur.execute("""
        #     CREATE TABLE IF NOT EXISTS users (
        #         id SERIAL PRIMARY KEY,
        #         username VARCHAR(80) UNIQUE NOT NULL,
        #         email VARCHAR(120) UNIQUE NOT NULL,
        #         password_hash VARCHAR(128) NOT NULL, -- Store hashed passwords!
        #         created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        #     );
        # """)
        conn.commit()
        print("Database schema initialized (or already exists).")
        cur.close()
    except psycopg2.Error as e:
        print(f"Error initializing database schema: {e}")
        conn.rollback()  # Rollback in case of error
    finally:
        if conn:
            conn.close()


@app.route("/ip_lookup", methods=["GET"])
def ip_lookup():
    ip_address = request.args.get("ip")
    if not ip_address:
        return jsonify({"error": "IP address is required"}), 400

    try:
        # It's good practice to use an API token for ipinfo.io in a real application
        # For now, we'll use the free tier without a token
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        data = response.json()
        return jsonify(data)
    except requests.exceptions.HTTPError as errh:
        return jsonify({"error": f"Http Error: {errh}"}), 500
    except requests.exceptions.ConnectionError as errc:
        return jsonify({"error": f"Error Connecting: {errc}"}), 500
    except requests.exceptions.Timeout as errt:
        return jsonify({"error": f"Timeout Error: {errt}"}), 500
    except requests.exceptions.RequestException as err:
        return jsonify({"error": f"Something went wrong: {err}"}), 500


@app.route("/scrape_twitter_profile", methods=["GET"])
def scrape_twitter_profile():
    username = request.args.get("username")
    if not username:
        return jsonify({"error": "Twitter username is required"}), 400

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    )

    profile_data = {}
    driver = None

    try:
        driver = webdriver.Chrome(options=chrome_options)
        # Construct the URL for the mobile version of Twitter for potentially simpler HTML
        # driver.get(f"https://mobile.twitter.com/{username}")
        driver.get(f"https://x.com/{username}")

        WebDriverWait(driver, 20).until(
            # Added fallback for main role
            EC.presence_of_element_located(
                (By.XPATH, "//div[@data-testid='primaryColumn'] | //main[@role='main']")
            )
        )

        # --- IMPORTANT: XPATHs below are EXAMPLES and WILL LIKELY BREAK ---
        # --- You MUST inspect the Twitter/X page and update these selectors ---

        try:
            # Example XPATH - Update this!
            # Looking for a span within a structure that usually holds the display name.
            name_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "//div[@data-testid='UserName']//span[1]//span[1] | //h2[@role='heading']/div/div/div/div/span",
                    )
                )
            )
            profile_data["name"] = name_element.text
        except Exception as e:
            profile_data["name"] = "Name not found (XPATH needs update)"
            print(f"Error scraping name: {e}")

        try:
            # Example XPATH - Update this!
            bio_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "//div[@data-testid='UserDescription'] | //div[contains(@data-testid, 'UserDescription')]",
                    )
                )
            )
            profile_data["bio"] = bio_element.text
        except Exception as e:
            profile_data["bio"] = "Bio not found (XPATH needs update)"
            print(f"Error scraping bio: {e}")

        try:
            # Example XPATH for followers - Update this!
            # This looks for an anchor tag whose href contains '/followers' and then finds a span with the numeric value.
            followers_link = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        f"//a[contains(@href, '/{username}/verified_followers')] | //a[contains(@href, '/{username}/followers')]",
                    )
                )
            )
            # The actual count is often in a span with specific styling or a data-testid.
            # This XPATH is a guess:
            followers_count_element = followers_link.find_element(
                By.XPATH,
                ".//span[contains(@data-testid, 'UserStatValue')] | .//span[1]/span[1]",
            )
            profile_data["followers"] = followers_count_element.text
        except Exception as e:
            profile_data["followers"] = "Followers count not found (XPATH needs update)"
            print(f"Error scraping followers: {e}")

        # --- Add more scraping logic for other data points here ---
        # Remember to use WebDriverWait and update XPATHs

        return jsonify(profile_data)

    except Exception as e:
        print(f"An error occurred during scraping: {e}")
        return jsonify({"error": f"Scraping failed: {str(e)}"}), 500
    finally:
        if driver:
            driver.quit()


@app.route("/api/search", methods=["POST"])
def handle_search():
    data = request.get_json()
    search_type = data.get("type")
    search_value = data.get("value")

    if not search_type or not search_value:
        return jsonify({"error": "Missing 'type' or 'value' in request"}), 400

    # Mock OSINT logic: return fake data for demo
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


if __name__ == "__main__":
    # It's good practice to initialize DB schema outside of app run,
    # but for simplicity in dev, we can call it here.
    # In a production setup, you might use a separate script or migration tool.
    print("Attempting to initialize database schema...")
    init_db()
    print("Starting Flask backend server...")
    # Make sure to run on 0.0.0.0 to be accessible from outside the container in Codespaces
    app.run(host="0.0.0.0", port=5001, debug=False)
