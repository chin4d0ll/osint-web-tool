import requests
from bs4 import BeautifulSoup


def scrape_tiktok(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return {"error": "TikTok profile not found"}

        soup = BeautifulSoup(response.text, "html.parser")
        description = soup.find("meta", {"name": "description"})["content"]
        return {
            "platform": "tiktok",
            "username": username,
            "profile_url": url,
            "bio": description,
            "followers": "N/A",
            "likes": "N/A",
        }
    except Exception as e:
        return {"error": str(e)}
