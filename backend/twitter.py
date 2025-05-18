def scrape_twitter(username):
    # ใช้ Nitter หรือ scraping แท้จริงได้ภายหลัง
    return {
        "platform": "twitter",
        "username": username,
        "profile_url": f"https://twitter.com/{username}",
        "bio": "Mock bio for Twitter",
        "followers": 123,
        "tweets": 456
    }