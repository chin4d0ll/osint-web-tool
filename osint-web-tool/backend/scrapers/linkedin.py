import requests
from bs4 import BeautifulSoup


def scrape_linkedin(name):
    query = f"site:linkedin.com/in/ {name}"
    url = f"https://duckduckgo.com/html/?q={query.replace(' ', '+')}"

    try:
        res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(res.text, "html.parser")
        links = soup.find_all("a", class_="result__a", href=True)
        results = [link["href"] for link in links if "linkedin.com/in/" in link["href"]]
        return {
            "platform": "linkedin",
            "query": name,
            "results": results[:5],  # Limit to top 5
        }
    except Exception as e:
        return {"error": str(e)}
