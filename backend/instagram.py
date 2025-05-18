from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


def scrape_instagram(username):
    url = f"https://www.instagram.com/{username}/"

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(5)

    result = {"platform": "instagram", "username": username, "profile_url": url}
    try:
        name_elem = driver.find_element(By.XPATH, "//header//h1")
        result["name"] = name_elem.text

        bio_elem = driver.find_element(By.XPATH, "//header//section/div[2]/span")
        result["bio"] = bio_elem.text

        stats = driver.find_elements(By.XPATH, "//header//li/span/span")
        if len(stats) >= 3:
            result["posts"] = stats[0].text
            result["followers"] = stats[1].text
            result["following"] = stats[2].text
    except Exception as e:
        result["error"] = str(e)

    driver.quit()
    return result
