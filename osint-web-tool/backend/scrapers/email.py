import requests

def scrape_email(email):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "hibp-api-key": "your_api_key_here"  # Replace with real API key
    }
    try:
        url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
        response = requests.get(url, headers=headers)
        if response.status_code == 404:
            return {"platform": "email", "email": email, "breaches": []}
        elif response.status_code == 200:
            data = response.json()
            return {
                "platform": "email",
                "email": email,
                "breaches": [item["Name"] for item in data]
            }
        else:
            return {"error": f"Status code {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}