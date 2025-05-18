import requests

def scrape_github(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": "GitHub user not found"}

    data = response.json()
    return {
        "platform": "github",
        "username": username,
        "profile_url": data.get("html_url"),
        "name": data.get("name"),
        "bio": data.get("bio"),
        "followers": data.get("followers"),
        "public_repos": data.get("public_repos"),
        "location": data.get("location")
    }