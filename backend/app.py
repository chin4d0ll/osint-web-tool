from flask import Flask, jsonify, request # Add request
from flask_cors import CORS
import requests # Add requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({"message": "OSINT Tool Backend Running"})

# New IP Lookup Endpoint
@app.route('/ip_lookup', methods=['GET'])
def ip_lookup():
    ip_address = request.args.get('ip')
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

@app.route('/scrape_twitter_profile', methods=['GET'])
def scrape_twitter_profile():
    username = request.args.get('username')
    if not username:
        return jsonify({"error": "Twitter username is required"}), 400

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

    profile_data = {}
    driver = None

    try:
        driver = webdriver.Chrome(options=chrome_options)
        # Construct the URL for the mobile version of Twitter for potentially simpler HTML
        # driver.get(f"https://mobile.twitter.com/{username}")
        driver.get(f"https://x.com/{username}")


        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-testid='primaryColumn'] | //main[@role='main']")) # Added fallback for main role
        )
        
        # --- IMPORTANT: XPATHs below are EXAMPLES and WILL LIKELY BREAK ---
        # --- You MUST inspect the Twitter/X page and update these selectors ---

        try:
            # Example XPATH - Update this!
            # Looking for a span within a structure that usually holds the display name.
            name_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='UserName']//span[1]//span[1] | //h2[@role='heading']/div/div/div/div/span"))
            )
            profile_data['name'] = name_element.text
        except Exception as e:
            profile_data['name'] = "Name not found (XPATH needs update)"
            print(f"Error scraping name: {e}")

        try:
            # Example XPATH - Update this!
            bio_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='UserDescription'] | //div[contains(@data-testid, 'UserDescription')]"))
            )
            profile_data['bio'] = bio_element.text
        except Exception as e:
            profile_data['bio'] = "Bio not found (XPATH needs update)"
            print(f"Error scraping bio: {e}")
            
        try:
            # Example XPATH for followers - Update this!
            # This looks for an anchor tag whose href contains '/followers' and then finds a span with the numeric value.
            followers_link = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, f"//a[contains(@href, '/{username}/verified_followers')] | //a[contains(@href, '/{username}/followers')]"))
            )
            # The actual count is often in a span with specific styling or a data-testid.
            # This XPATH is a guess:
            followers_count_element = followers_link.find_element(By.XPATH, ".//span[contains(@data-testid, 'UserStatValue')] | .//span[1]/span[1]")
            profile_data['followers'] = followers_count_element.text
        except Exception as e:
            profile_data['followers'] = "Followers count not found (XPATH needs update)"
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001) # Changed port to 5001
