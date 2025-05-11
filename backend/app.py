from flask import Flask, jsonify, request # Add request
from flask_cors import CORS
import requests # Add requests

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
